import database
from database import SQL_Data
# Basic logic; calculate the 
#    priceT = 0
#    priceY = 0
#    x = (pT - pY)
#    prediction = priceY + x
#    accuracy = priceT - prediction

# Global Variables.
read = SQL_Data()
item_list = []
priceT = 0
priceY = 0
date = ""
price_yesterday = {}
price_today = {}

def appender(timestamp, name):        
    priceY = 0
    priceT = 0
    price = timestamp[1]
    price = timestamp[-1]
    if name in price_today:
        priceY = price_today[name]
        price_yesterday[name] = priceY
        priceT = price_today[name]
    else:
        priceT = price_yesterday[name]
        price_today[name] = priceT
    x = float(priceY) - float(priceT)
    prediction = priceT + x
    print(f"{name}, price today: {priceT}, predicition: {prediction}")

#Create a list of items and data.

for timestamp in read.datadump:  
    name = timestamp[1]
    if not name in item_list:
        item_list.append(name)
    price_today[name] = timestamp[-1]
    appender(timestamp, name)
