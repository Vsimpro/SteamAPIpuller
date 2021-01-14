import database
import time
from database import SQL_Data
from flask import Flask, render_template
app = Flask(__name__)

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
prediction_list = {}

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
    prediction_list[name] = prediction

def main():
#Create a list of items and data.
    for timestamp in read.datadump:  
        name = timestamp[1]
        if not name in item_list:
            item_list.append(name)
        price_today[name] = timestamp[-1]
        appender(timestamp, name)


@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/predictions')
def home_button():
    main()
    predictions = ""
    for i in prediction_list:
        space = len("Winter Offensive Weapon")
        spacer = len(i) - space
        breaker = spacer * " "
        allPredictions = f"Case: {i} will tomorrow be:{breaker} {prediction_list[i]}€ <br>"
        predictions += allPredictions
    return render_template('predictions.html', variable=predictions)

@app.route('/robots.txt/')
def robots():
    return "ladies and gentlemen, we got him."


if __name__ == "__main__":
    app.run(host='0.0.0.0')
    main()