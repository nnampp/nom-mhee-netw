#!/bin/bash
cd C:\xampp\mysql

mysql -u root -p


use mqtt_subscriber_db

sql='SELECT * FROM mqtt_subscriber_db'
echo ${sql}