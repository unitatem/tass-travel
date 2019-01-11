import csv

from tools.database import Database


class FlightParser:
    def __init__(self, path):
        self._path = path
        self._city = {}
        self._airport = {}
        self._db = Database()

    def parse_and_insert(self):
        with open(self._path, newline='') as csv_file:
            self._db.open_transaction()

            reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            for row in reader:
                try:
                    org_airport_code = row[0]
                    dst_airport_code = row[1]
                    org_city_name = row[2]
                    dst_city_name = row[3]
                    passengers = int(row[4])
                    seats = int(row[5])
                    flights = int(row[6])
                    distance = int(row[7])
                    fly_data = row[8]
                    org_city_population = int(row[9])
                    dst_city_population = int(row[10])
                    org_airport_lat = float(row[11])
                    org_airport_lng = float(row[12])
                    dst_airport_lat = float(row[13])
                    dst_airport_lng = float(row[14])

                    self._insert_city(org_city_name, org_city_population)
                    self._insert_city(dst_city_name, dst_city_population)

                    self._insert_airport(org_airport_code, org_airport_lat, org_airport_lng)
                    self._insert_airport(dst_airport_code, dst_airport_lat, dst_airport_lng)

                    self._db.insert_flight(self._city[org_city_name], self._airport[org_airport_code],
                                           self._city[dst_city_name], self._airport[dst_airport_code],
                                           passengers, seats, flights, distance, fly_data)
                except ValueError as error:
                    # print("ValueError:", row)
                    print(error)
                    continue

            self._db.close_transaction()

    def _insert_city(self, name, population):
        idx = self._db.insert_city(name, population)
        if idx is not None:
            self._city[name] = idx

    def _insert_airport(self, code, lat, lng):
        idx = self._db.insert_airport(code, lat, lng)
        if idx is not None:
            self._airport[code] = idx


if __name__ == "__main__":
    parser = FlightParser('../resources/Airports2.csv')
    parser.parse_and_insert()
