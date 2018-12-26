# tass-travel
Finds best travel destinations based on user preferences

# Dependencies
https://www.postgresql.org/  

```bash
sudo apt-get install postgresql postgresql-contrib
```

# Resources
https://www.kaggle.com/flashgordon/usa-airport-dataset  
http://www.overpass-api.de/ - API for OSM access

# Usage
Prepare database
```bash
cd src
python3 download_resources.py
./setup_db.sh
python3 flight_parser.py
python3 poi_cnt_updater.py
```
