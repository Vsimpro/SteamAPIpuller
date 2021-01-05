#!/usr/bin/python

import sqlite3
import re

def create(items):
    connection = sqlite3.connect('alkonhyllyt.db')
    connection.execute('''CREATE TABLE IF NOT EXISTS Data (ID INTEGER PRIMARY KEY, timestamp TEXT, name TEXT, lowest_price INT, volume INT, median_price INT);''')
    
    records = []
    for item in items:
        list_of_attributes = []
        for key in item:
            list_of_attributes.append(item[key])
        records.append(list_of_attributes)

    connection.execute('INSERT INTO Data VALUES (?,?,?,?,?);', records)
    connection.commit()
    connection.close()

def read():
    cursor = sqlite3.connect('alkonhyllyt.db').cursor()
    cursor.execute('''SELECT timestamp, name, lowest_price, volume, median_price FROM Data;''')
    print(cursor.fetchall())

read()