from pathlib import Path


def exist(path):
    file = Path(path)
    if file.is_file():
        return True
    return False


def download():
    path = "../resources/Airports2.csv"
    if not exist(path):
        raise Exception("Please download and extract dataset from Kaggle: "
                        "https://www.kaggle.com/flashgordon/usa-airport-dataset")
    print("Ready to go")
    return 0


if __name__ == "__main__":
    download()
