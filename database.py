#!/usr/bin/python

import sqlite3
import re

def create(incoming_dictionary):
    connection = sqlite3.connect('alkonhyllyt.db')
    connection.execute('''CREATE TABLE IF NOT EXISTS Data (ID INTEGER PRIMARY KEY, timestamp TEXT, name TEXT, lowest_price INT, volume INT, median_price INT);''')
    timestamp = list(incoming_dictionary.keys())[0]
    item_list = list(incoming_dictionary.values())[0].split("\n")
    
    for item in item_list:
        for attribute in re.split(' lowest |: |\n',item):
            print(attribute)
    connection.execute('''INSERT INTO Data (timestamp, name, lowest_price, volume, median_price)\
        VALUES ('2021-01-05-14:58', 'Prisma Case', 1,2,3);''')
    connection.commit()
    connection.close()

def read():
    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    con = sqlite3.connect('alkonhyllyt.db')
    con.row_factory = dict_factory
    cur = con.cursor()
    cur.execute("select 1 as a")
    print (cur.fetchone()["a"])

create({'2021-01-05-15:19': 'Prisma lowest price: 0,04? volume: 77,079 median price: 0,02? Prisma2 lowest price: 0,04? volume: 71,748 median price: 0,02? Revolver lowest price: 0,05? volume: 17,433 median price: 0,05? Danger Zone lowest price: 0,05? volume: 112,516 median price: 0,03? Horizon Case lowest price: 0,05? volume: 34,229 median price: 0,05? '})