#!/bin/bash

RED='\033[0;31m'
NC='\033[0m'
function ECHO {
	echo -e ${RED}"\n"$1"\n"${NC}
}

ECHO "crate user tass"
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

    CREATE TABLE city(id SERIAL NOT NULL PRIMARY KEY,
                      name VARCHAR(255) NOT NULL UNIQUE,
                      population INT NOT NULL) ;

    CREATE TABLE airport(id SERIAL NOT NULL PRIMARY KEY,
                         code CHAR(3) NOT NULL UNIQUE,
                         latitude FLOAT NOT NULL,
                         longitude FLOAT NOT NULL) ;

    CREATE TABLE flight(id SERIAL NOT NULL PRIMARY KEY,
                        org_city INTEGER NOT NULL REFERENCES city (id),
                        org_airport INTEGER NOT NULL REFERENCES airport (id),
                        dst_city INTEGER NOT NULL REFERENCES city (id),
                        dst_airport INTEGER NOT NULL REFERENCES airport (id),
                        passengers INT NOT NULL,
                        seats INT NOT NULL,
                        flights INT NOT NULL,
                        distance INT NOT NULL,
                        fly_date DATE NOT NULL) ;

     CREATE TABLE poi(id SERIAL NOT NULL PRIMARY KEY,
                      city INTEGER NOT NULL REFERENCES city (id),
                      name VARCHAR(255) NOT NULL,
                      type VARCHAR(255) NOT NULL,
                      value VARCHAR(255) NOT NULL) ;
EOF

ECHO "DONE"
