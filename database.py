#!/usr/bin/python

import sqlite3
import re

def create(items):
    connection = sqlite3.connect('alkonhyllyt.db')
    connection.execute('''CREATE TABLE IF NOT EXISTS Data (ID INT PRIMARY KEY, lowest_price REAL, volume INT, median_price REAL, name TEXT, timestamp TEXT);''')
    
    records = []
    for item_dictionary in items:
        list_of_attributes = []
        for key in item_dictionary.keys():
            value = item_dictionary[key]
            if key=='success':
                continue
            elif key=='lowest_price':
                value = float(value.replace('?','').replace(',','.'))
            elif key=='volume':
                value = int(value.replace(',',''))
            elif key=='median_price':
                value = float(value.replace(',','.').replace('?',''))
            list_of_attributes.append(value)
        print(list_of_attributes)
        records.append(list_of_attributes)

    connection.executemany('INSERT INTO Data(lowest_price, volume, median_price, name, timestamp) VALUES (?,?,?,?,?);', records)
    connection.commit()
    connection.close()

def read():
    cursor = sqlite3.connect('alkonhyllyt.db').cursor()
    cursor.execute('''SELECT timestamp, name, lowest_price, volume, median_price FROM Data;''')
    print(cursor.fetchall())

create([{'success': True, 'lowest_price': '0,09?', 'volume': '11,879', 'median_price': '0,09?', 'Name': 'Chroma 2', 'Timestamp': '2021-01-07-23:49'},{'success': True, 'lowest_price': '0,03?', 'volume': '13,831', 'median_price': '0,03?', 'Name': 'Muna seinalla', 'Timestamp': '2021-05-07-23:49'}])