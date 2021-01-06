#! python3 scraper.py

import requests
import json
import datetime
import time
import threading
import os
import commandline
from datetime import date

# There is currently print commands scattered around the project, 
# Simply to ease the debug process.

# Global variables.
today = date.today()
counter = []
output_gap = 30

# Pre-define skin / item names and their hash names here.
item_list = {"Chroma 2":"Chroma%202%20Case", "Chroma 3":"Chroma%203%20Case", "Clutch":"Clutch%20Case", "CS20":"CS20%20Case", "Danger Zone":"Danger%20Zone%20Case",
"Falchion":"Falchion%20Case", "Fracture":"Fracture%20Case", "Gamma":"Gamma%20Case", "Gamma 2":"Gamma%202%20Case", "Glove":"Glove%20Case", "Horizon":"Horizon%20Case", 
"Huntsman":"Huntsman%20Weapon%20Case", "Operation Bravo":"Operation%20Bravo%20Case", "Operation Breakout Weapon":"Operation%20Breakout%20Weapon%20Case",
"Operation Broken Fang":"Operation%20Broken%20Fang%20Case","Operation Hydra":"Operation%20Hydra%20Case", "Operation Phoenix Weapon":"Operation%20Phoenix%20Weapon%20Case",
"Operation Vanguard Weapon":"Operation%20Vanguard%20Weapon%20Case", "Operation Wildfire":"Operation%20Wildfire%20Case", "Prisma":"Prisma%20Case",
"Prisma 2":"Prisma%202%20Case", "Revolver":"Revolver%20Case", "Shadow":"Shadow%20Case", "Shattered Web":"Shattered%20Web%20Case",
"Spectrum":"Spectrum%20Case", "Spectrum 2":"Spectrum%202%20Case", "Winter Offensive Weapon":"Winter%20Offensive%20Weapon%20Case"}

# Stores the data with a date and time.
datastore = []
datapoint = {}

# Call this function as wait(desired time to wait), and format it in seconds.
def wait(timer):
    time.sleep(timer)

# Store the data.
def database(data):
    datastore.append(data)

# Pull the data from Steam "API".
def puller():
    pulled_items = []
    for item in item_list:
        pulled_items.append(item)
        url = (f"http://steamcommunity.com/market/priceoverview/?appid=730&market_hash_name={item_list[item]}&currency=3")
        pull = requests.get(url)
        data = json.loads(pull.content)
        timer = 5
        wait(timer)
        while True:  
          if data == None:
            print(f"Error in: json.loads((requests.get(url)).content), datavalue is: {data}")
            print(f"Item: {item}")
            wait(timer)
          elif data["success"] == False:
            print(f"COULD NOT PULL {item}, check it's hashname!")
            break    
          else: 
            data["Name"] = item
            dt = datetime.datetime.now()
            data["Timestamp"] = dt.strftime("%Y-%m-%d-%H:%M")
            space = " "
            gap_for_item = output_gap - len(item)
            space = space * gap_for_item
            print(f"Data for item {item}:{space}{data}")
            database(data)
            break

# Test database.
def print_database():
    counter = 0
    with open("backlog.txt", "a", encoding="utf-8") as file:
        timetag = ""

        file.write(timetag)
        for record in datastore:
            #file.write(record)
            for key in record:
                file.write(key)
                file.write(":")
                backlog = str(record[key])
                file.write(backlog)
                file.write("\n")
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
                    print("Continuing what ever I was doing.")
                    break
                else:
                    pass
        else:
            print("This should pop out.")
            commandline.main(user)
# Loops the pulling process.
def loop():
    while True:
        counter.append(1)
        puller()
        print(f"Data received for desired items.\n")
        timer = 120
        wait(timer)
# Gives pulling process it's own thread, while going into a while loop for userconsole.
def main():
    mainthread = threading.Thread(target=loop)
    mainthread.start()
    userconsole()
if __name__ =="__main__":
    main()
