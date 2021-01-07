#! python3 scraper.py

import requests
import json
import datetime
import time
import threading
import os
import commandline
import database
from datetime import date

# There is currently print commands scattered around the project, 
# Simply to ease the debug process.

# Global variables.
today = date.today()
counter = []

# Pre-define skin / item names and their hash names here.
item_list = {"Chroma 2":"Chroma%202%20Case"}

# Stores the data with a date and time.
datastore = []

# Pull the data from Steam "API".
def puller():
    for item in item_list:
        time.sleep(5)
        while True:
            url = (f"http://steamcommunity.com/market/priceoverview/?appid=730&market_hash_name={item_list[item]}&currency=3")
            pull = requests.get(url)
            data = json.loads(pull.content)
            if data == None:
                print(f"Error: datavalue is: {data}\nThis might be due to too many pull requests.\nItem: {item}")
                time.sleep(5)
                pass
            elif data["success"] == False:
                print(f"COULD NOT PULL {item}, check it's hashname!")
                break    
            else: 
                data["Name"] = item
                dt = datetime.datetime.now()
                data["Timestamp"] = dt.strftime("%Y-%m-%d-%H:%M")
                space = " "
                outputgap= 30 - len(item)
                space = space * outputgap
                #print(f"Data for item {item}:{space}{data}")
                datastore.append(data)
                break

# Test database.
def print_database():
    # database.create(datastore)
    with open("backlog.txt", "a", encoding="utf-8") as file:
        #for record in datastore:
        point = str(datastore)
        file.write(point)
    print(f"Data stored to backlog.")

# This console gives the user an ability to interact with the scraper.
def userconsole():
    commandline.commandOpenMsg()
    while True:
        user = input("")
        if user == "exit":
            commandline.areYouSureMSG()
            while True:
                print("yes / no")
                user = input("")
                if user == "yes":
                    print_database()
                    os._exit(1)
                elif user == "no":
                    print("Continuing.")
                    break
                else:
                    pass
        else:
            commandline.main(user)

# Loops the pulling process.
def loop():
    while True:
        counter.append(1)
        puller()
        print(f"Data received for desired items.")
        print_database()
        time.sleep(14000)
        
# Gives pulling process it's own thread, while going into a while loop for userconsole.
def main():
    mainthread = threading.Thread(target=loop)
    mainthread.start()
    userconsole()

if __name__ =="__main__":
    main()
