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

    # PostGIS encodes coordinates as Mercator projection (ref: http://openstreetmapdata.com/info/projections).
    # Mercator Projection is known as EPSG 3857 (units: meters).
    #
    # Google Maps use WGS84 known as EPSG 4326 (former 900913 (Google in numeric AWESOME)) (units: degrees).
    #
    # PostGIS encodes longitude as x coordinate and latitude as y coordinate.
    #
    # SQL query below prints: osm_id, name, latitude, longitude and distance (from hardcoded point)
    # for points classified as cafe in distance below 2500 meters from hardcoded point.

    # SELECT
    # osm_id,
    # name,
    # ST_Y(ST_Transform(way, 4326)) AS lat,
    # ST_X(ST_Transform(way, 4326)) AS lng,
    # ST_Distance(way,
    #             ST_TRANSFORM(ST_SETSRID(ST_MAKEPOINT(7.41777639896744, 43.732650195099), 4326), 3857)) as dist
    # FROM planet_osm_point
    # WHERE amenity = 'cafe' AND ST_DWITHIN(way,
    # 				      ST_TRANSFORM(ST_SETSRID(ST_MAKEPOINT(7.41777639896744, 43.732650195099), 4326), 3857), 2500);

    def get_poi_count(self, lat: float, lng: float, radius: float):
        self._check_cursor()

        sql = """
        SELECT COUNT(*)
        FROM planet_osm_point
        WHERE amenity = 'cafe'
            AND ST_DWITHIN(way,
                           ST_TRANSFORM(ST_SETSRID(ST_MAKEPOINT({longitude}, {latitude}),
                                                   4326),
                                        3857),
                           {radius})
        """.format(latitude=lat,
                   longitude=lng,
                   radius=radius)
        self._cursor.execute(sql)
        return self._safe_fetchone()

    def get_all_cities(self):
        self._check_cursor()

        sql = """
        SELECT * FROM city
        """
        self._cursor.execute(sql)
        rows = self._cursor.fetchall()
        rows = [{'id': r[0], 'name': r[1], 'population': r[2]} for r in rows]
        return rows

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
