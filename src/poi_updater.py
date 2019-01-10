import random
import time

from database import Database
from osm_api import OSM


class PoiUpdater:
    def __init__(self, radius: int):
        self._radius = radius
        self._db = Database()
        self._osm = OSM()

    def update(self):
        self._db.open_transaction()

        cities = self._db.get_all_cities()
        city_local_geo = self._db.get_all_cities_one_airport_geo()
        for city in cities:
            if self._db.count_poi(city['id']) != 0:
                continue
            c = city['name'].split(", ")
            city_name = c[0]
            print(city_name + ' ', end='', flush=True)

            pois = self._osm.get_pois(city_name,
                                      city_local_geo[city['id']],
                                      self._radius)
            print(len(pois))
            if len(pois) == 0:
                print("Sth gone wrong:", city)
            for poi in pois:
                self._db.insert_poi(city['id'], poi)
            # just in case, try to prevent ban
            time.sleep(random.uniform(0.1, 1))

        self._db.close_transaction()

    def invalid_cities(self):
        self._db.open_transaction()

        cities = self._db.get_all_cities()
        invalid_city = []
        for city in cities:
            if self._db.count_poi(city['id']) == 0:
                invalid_city.append(city)

        self._db.close_transaction()
        return invalid_city


def main():
    pu = PoiUpdater(20000)
    pu.update()
    print("Done")
    invalid_cities = pu.invalid_cities()
    for c in invalid_cities:
        print(c)


if __name__ == "__main__":
    main()
