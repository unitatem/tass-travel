import psycopg2


class Database:
    def __init__(self):
        self._connection = None
        self._cursor = None

        self._connect()

    def __del__(self):
        print("Database finalizer called")
        if self._cursor is not None:
            self._cursor.close()
        if self._connection is not None:
            self._connection.commit()
            self._connection.close()

    def open_transaction(self):
        if self._connection is None:
            raise RuntimeError("Database connection to DB is not initialized properly")
        if self._cursor is not None:
            raise RuntimeError("Transaction is already open")
        self._cursor = self._connection.cursor()

    def close_transaction(self):
        self._check_cursor()

        self._connection.commit()
        self._cursor.close()
        self._cursor = None

    def _check_cursor(self):
        if self._cursor is None:
            raise RuntimeError("Transaction is already closed")

    def _connect(self):
        print('Connecting to the PostgreSQL database...')
        self._connection = psycopg2.connect(user="tass",
                                            password="tass",
                                            host="localhost",
                                            database="tass_db")

    def insert_city(self, name: str, population: int):
        self._check_cursor()

        sql = """
        INSERT INTO city(name, population) VALUES(%s, %s)
        ON CONFLICT DO NOTHING
        RETURNING id"""
        self._cursor.execute(sql, (name, population))
        return self._safe_fetchone()

    def _safe_fetchone(self):
        ret = self._cursor.fetchone()
        if ret is None:
            return None
        return ret[0]

    def get_all_cities(self):
        self._check_cursor()

        sql = """
        SELECT * FROM city
        """
        self._cursor.execute(sql)
        rows = self._cursor.fetchall()
        rows = [{'id': r[0], 'name': r[1], 'population': r[2], 'poi_cnt': r[3]} for r in rows]
        return rows

    def get_all_cities_one_airport_geo(self):
        self._check_cursor()

        sql = """
        SELECT DISTINCT f.dst_city, a.latitude, a.longitude
        FROM flight f
            LEFT JOIN airport a on f.dst_airport = a.id
        """
        self._cursor.execute(sql)
        rows = self._cursor.fetchall()
        result = {}
        for r in rows:
            result[r[0]] = {'lat': r[1], 'lng': r[2]}
        return result

    def update_city_poi_cnt(self, id: int, cnt: int):
        self._check_cursor()

        sql = """
        UPDATE city
        SET poi_cnt = '{cnt}'
        WHERE id = '{id}' ;
        """.format(cnt=cnt,
                   id=id)
        self._cursor.execute(sql)

    def insert_airport(self, code: str, latitude: float, longitude: float):
        self._check_cursor()

        sql = """
        INSERT INTO airport(code, latitude, longitude) VALUES(%s, %s, %s)
        ON CONFLICT DO NOTHING
        RETURNING id"""
        self._cursor.execute(sql, (code, latitude, longitude))
        return self._safe_fetchone()

    def insert_flight(self, org_city: int, org_airport: int, dst_city: int, dst_airport: int,
                      passengers: int, seats: int, flights: int, distance: int, date: str):
        self._check_cursor()

        sql = """
        INSERT INTO flight(org_city, org_airport, dst_city, dst_airport,
                           passengers, seats, flights, distance, fly_date)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        self._cursor.execute(sql, (org_city, org_airport, dst_city, dst_airport,
                                   passengers, seats, flights, distance, date))

    def get_flights(self, begin_date: str, end_end: str):
        """
        Please provide date in format YYYY-MM-DD
        """
        self._check_cursor()

        sql = """
        SELECT org_city, dst_city, SUM(passengers)
        FROM flight
        WHERE fly_date >= '{begin}'
            AND fly_date < '{end}'
            AND passengers > 0
        GROUP BY org_city, dst_city
        """.format(begin=begin_date,
                   end=end_end)
        self._cursor.execute(sql)
        rows = self._cursor.fetchall()
        rows = [{'from': r[0], 'to': r[1], 'passengers': r[2]} for r in rows]
        return rows
