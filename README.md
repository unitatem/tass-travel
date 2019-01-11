# tass-travel
Finds best travel destinations based on user preferences

# Dependencies
### PostgreSQL
https://www.postgresql.org/  
```bash
sudo apt-get install postgresql postgresql-contrib
```

### PyQt5
https://pypi.org/project/PyQt5/
```bash
sudo apt install qtcreator
```

For conversion of *.ui into *.py
```bash
pyuic5 -x file.ui -o file.py
```

# Resources
https://www.kaggle.com/flashgordon/usa-airport-dataset  
http://www.overpass-api.de/ - API for OSM access

# Usage
Prepare database
```bash
cd tass_travel
python3 setup/download_resources.py
setup/setup_db.sh
python3 setup/flight_parser.py
python3 setup/poi_updater.py
```
