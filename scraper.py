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
item_list = {"Chroma 2":"Chroma%202%20Case", "Chroma 3":"Chroma%203%20Case", "Clutch":"Clutch%20Case", "CS20":"CS20%20Case", "Danger Zone":"Danger%20Zone%20Case",
"Falchion":"Falchion%20Case", "Fracture":"Fracture%20Case", "Gamma":"Gamma%20Case", "Gamma 2":"Gamma%202%20Case", "Glove":"Glove%20Case", "Horizon":"Horizon%20Case", 
"Huntsman":"Huntsman%20Weapon%20Case", "Operation Bravo":"Operation%20Bravo%20Case", "Operation Breakout Weapon":"Operation%20Breakout%20Weapon%20Case",
"Operation Broken Fang":"Operation%20Broken%20Fang%20Case","Operation Hydra":"Operation%20Hydra%20Case", "Operation Phoenix Weapon":"Operation%20Phoenix%20Weapon%20Case",
"Operation Vanguard Weapon":"Operation%20Vanguard%20Weapon%20Case", "Operation Wildfire":"Operation%20Wildfire%20Case", "Prisma":"Prisma%20Case",
"Prisma 2":"Prisma%202%20Case", "Revolver":"Revolver%20Case", "Shadow":"Shadow%20Case", "Shattered Web":"Shattered%20Web%20Case",
"Spectrum":"Spectrum%20Case", "Spectrum 2":"Spectrum%202%20Case", "Winter Offensive Weapon":"Winter%20Offensive%20Weapon%20Case"}

# Stores the data with a date and time.
datastore = []

# Pull the data from Steam "API".
def puller():
    for item in item_list:
        while True:
            url = (f"http://steamcommunity.com/market/priceoverview/?appid=730&market_hash_name={item_list[item]}&currency=3")
            pull = requests.get(url)
            data = json.loads(pull.content)
            time.sleep(5)
            if data == None:
                print(f"Error: datavalue is: {data}\nThis might be due to too many pull requests.\nItem: {item}")
                time.sleep(5)
                pass
            elif data["success"] == False:
                print(f"COULD NOT PULL {item}, check it's hashname!")     
                break    
            else: 
                counter.append(1)
                data["Name"] = item
                dt = datetime.datetime.now()
                data["Timestamp"] = dt.strftime("%Y-%m-%d-%H:%M")
                space = " "
                outputgap= 30 - len(item)
                space = space * outputgap
                print(f"Data for item {data}")
                datastore.append(data)
                break

# Test database.
def print_database():
    database.create(datastore)

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
