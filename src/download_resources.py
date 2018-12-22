import urllib.request
from pathlib import Path


def exist(path):
    file = Path(path)
    if file.is_file():
        return True
    return False


def download_and_save(url, destination):
    urllib.request.urlretrieve(url, destination)


def download():
    path = "../resources/Airports2.csv"
    if not exist(path):
        raise Exception("Please download and extract dataset from Kaggle: "
                        "https://www.kaggle.com/flashgordon/usa-airport-dataset")

    path = "../resources/north-america.osm.pbf"
    if not exist(path):
        print("Downloading OSM (8 GB) ...")
        download_and_save("http://download.openstreetmap.fr/extracts/north-america.osm.pbf",
                          path)

    print("Ready to go")
    return 0


if __name__ == "__main__":
    download()
