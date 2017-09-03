#!/bin/sh
mongoimport --db weisheng --collection hygiene --type csv --headerline --file ../data/DOHMH_New_York_City_Restaurant_Inspection_Results_1.csv
mongoimport --db weisheng --collection hygiene --type csv --headerline --file ../data/DOHMH_New_York_City_Restaurant_Inspection_Results_2.csv
mongoimport --db weisheng --collection yelpDataMain --type json --file ../data/yelpDataMain.json
