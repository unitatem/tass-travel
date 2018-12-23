from database import Database


def main():
    db = Database()
    db.open_transaction()

    lat = 43.732650195099
    lng = 7.41777639896744
    count = db.get_poi_count(lat, lng, 2500)
    print("count:", count)

    db.close_transaction()


if __name__ == '__main__':
    main()
