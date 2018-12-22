#!/bin/bash

if [[ "$1" != "" ]]; then
    OSM_FILE=$1
else
    OSM_FILE=monaco.osm.pbf
fi


RED='\033[0;31m'
NC='\033[0m'
function ECHO {
	echo -e $RED"\n"$1"\n"$NC
}

ECHO "crate user tass (password=tass)"
sudo su - postgres -c '
	createuser tass
	psql -c "ALTER USER tass WITH SUPERUSER CREATEDB PASSWORD '\''tass'\''" ;
	psql -c "\du"
	psql -c "\l"
'

ECHO "create tass_db (password=tass)"
psql -U tass -h localhost -d postgres << EOF
	CREATE DATABASE tass_db ;
	\c tass_db
	CREATE EXTENSION postgis ;
EOF

ECHO "load osm data"
osm2pgsql -s -U tass -W -H localhost -d tass_db ../resources/${OSM_FILE}

echo DONE

