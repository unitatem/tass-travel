import psycopg2


class Database:
    def __init__(self):
        self._connection = None
        self._cursor = None

        self._connect()

    def __del__(self):
        print("Database finalizer called")
        if self._connection is not None:
            self._connection.close()

    def open_transaction(self):
        if self._connection is None:
            raise RuntimeError("Database connection to DB is not initialized properly")
        if self._cursor is not None:
            raise RuntimeError("Transaction is already open")
        self._cursor = self._connection.cursor()

    def close_transaction(self):
        if self._cursor is None:
            raise RuntimeError("Transaction is already closed")
        self._connection.commit()
        self._cursor.close()
        self._cursor = None

    def _connect(self):
        print('Connecting to the PostgreSQL database...')
        self._connection = psycopg2.connect(user="tass",
                                            password="tass",
                                            host="localhost",
                                            database="tass_db")
        print("Done")

    def insert_city(self, name: str, population: int):
        if self._cursor is None:
            raise RuntimeError("Transaction is already closed")

        sql = "INSERT INTO city(name, population) VALUES(%s, %s) " \
              "ON CONFLICT DO NOTHING " \
              "RETURNING id"
        self._cursor.execute(sql, (name, population))

        ret = self._cursor.fetchone()
        if ret is None:
            return None
        return ret[0]

    def insert_airport(self, code: str, latitude: float, longitude: float):
        if self._cursor is None:
            raise RuntimeError("Transaction is already closed")

        sql = "INSERT INTO airport(code, latitude, longitude) VALUES(%s, %s, %s) " \
              "ON CONFLICT DO NOTHING " \
              "RETURNING id"
        self._cursor.execute(sql, (code, latitude, longitude))

        ret = self._cursor.fetchone()
        if ret is None:
            return None
        return ret[0]

    def insert_flight(self, org_city: int, org_airport: int, dst_city: int, dst_airport: int,
                      passengers: int, seats: int, flights: int, distance: int, date: str):
        if self._cursor is None:
            raise RuntimeError("Transaction is already closed")

        sql = "INSERT INTO flight(org_city, org_airport, dst_city, dst_airport, " \
              "passengers, seats, flights, distance, fly_date) " \
              "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s) "
        self._cursor.execute(sql, (org_city, org_airport, dst_city, dst_airport,
                                   passengers, seats, flights, distance, date))
