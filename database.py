#!/usr/bin/python

import sqlite3
import re

class SQL_Data():
    def __init__(self):
        cursor = sqlite3.connect('alkonhyllyt.db').cursor()
        cursor.execute('''SELECT timestamp, name, lowest_price, volume, median_price FROM Data;''')
        #datadump = cursor.fetchall()
        self.datadump = cursor.fetchall()

def create(items):
    connection = sqlite3.connect('alkonhyllyt.db')
    connection.execute('''CREATE TABLE IF NOT EXISTS Data (ID INTEGER PRIMARY KEY, lowest_price REAL, volume INT, median_price REAL, name TEXT, timestamp TEXT);''')
    
    records = []
    for item_dictionary in items:
        list_of_attributes = []
        for key in item_dictionary.keys():
            value = item_dictionary[key]
            if key=='success':
                continue
            elif key=='lowest_price':
                value = float(value.replace('€','').replace(',','.'))
            elif key=='volume':
                value = int(value.replace(',',''))
            elif key=='median_price':
                value = float(value.replace(',','.').replace('€',''))
            list_of_attributes.append(value)
        records.append(list_of_attributes)

    connection.executemany('INSERT INTO Data(lowest_price, volume, median_price, name, timestamp) VALUES (?,?,?,?,?);', records)
    connection.commit()
    connection.close()

def read():
    cursor = sqlite3.connect('alkonhyllyt.db').cursor()
    cursor.execute('''SELECT timestamp, name, lowest_price, volume, median_price FROM Data;''')