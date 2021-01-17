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
    if name in price_today:
        priceT = price_today[name]
    else:
        priceT = 0
    
    if name in price_yesterday:
        priceY = price_yesterday[name]
    else:
        priceY = 0
    
    x = float(priceT) - float(priceY)
    prediction = priceT + x
    prediction_list[name] = prediction 
    price_yesterday[name] = price_today[name]

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
def display_predictions():
    main()
    predictions = ""
    for i in prediction_list:
        case = i.replace("Operation","")
        case = i.replace("Weapon","")
        pred4tomorrow = round(prediction_list[i], 2)
        allPredictions = f"{case} will be: {pred4tomorrow}€ <br>"
        predictions += allPredictions
        header =  "And I predict --the prices for tomorrow are.."
    return render_template('predictions.html', variable=header , pricepredicts=predictions)

@app.route('/prices')
def prices_rn():
    prices = ""
    main()
    datadct = {}
    for key in read.datadump:
        pulldate = key[0]
        name = key[1]
        datadct[name]  = key[-1]
    for name in datadct:    
        itemdata = f"{name} Case: {datadct[name]}€ <br>"
        prices += itemdata
    return render_template('prices.html', variable=f"Last pull {pulldate}", pricepredicts=prices )


if __name__ == "__main__":
    app.run(host='0.0.0.0')
    main()