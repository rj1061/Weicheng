#!/bin/sh
mongoimport --db weisheng --collection hygiene --type csv --headerline --file /home/leo/Downloads/DOHMH_New_York_City_Restaurant_Inspection_Results.csv
