import urllib.request
from pathlib import Path


def if_exist(path):
    file = Path(path)
    if file.is_file():
        return True
    return False


def download_and_save(url, destination):
    urllib.request.urlretrieve(url, destination)


def main():
    path = "../resources/Airports2.csv"
    if not if_exist(path):
        print("Please download and extract dataset from Kaggle: "
              "https://www.kaggle.com/flashgordon/usa-airport-dataset")

    path = "../resources/north-america.osm.pbf"
    if not if_exist(path):
        print("Downloading OSM (8 GB) ...")
        download_and_save("http://download.openstreetmap.fr/extracts/north-america.osm.pbf",
                          path)

    print("Ready to go")
    return 0


if __name__ == "__main__":
    main()
