import random
import time

from database import Database
from osm_api import OSM


class PoiCntUpdater:
    def __init__(self, radius: int):
        self._radius = radius
        self._db = Database()
        self._osm = OSM()

    def update(self):
        self._db.open_transaction()

        cities = self._db.get_all_cities()
        city_local_geo = self._db.get_all_cities_one_airport_geo()
        for city in cities:
            c = city['name'].split(", ")
            city_name = c[0]
            print(city_name)

            cnt = self._osm.get_poi_cnt_for_city(city_name,
                                                 city_local_geo[city['id']],
                                                 self._radius)
            if cnt == 0:
                print("Sth gone wrong: ", city)
            self._db.update_city_poi_cnt(city['id'], cnt)
            # just in case try to prevent ban
            time.sleep(random.randint(1, 10))

        self._db.close_transaction()


if __name__ == "__main__":
    pcu = PoiCntUpdater(20000)
    pcu.update()
    print("Done")
