#!/bin/sh
sh ./data_clean/import_data.sh
mongo < ./data_clean/hygiene_data_clean.js
mongo < ./mapreduce/mapReduce.js
python ./data_clean/yelp_hygiene_join.py
