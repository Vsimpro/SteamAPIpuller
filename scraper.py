#! python3 scraper.py

import requests
import json
import datetime
import time
import threading
import os
from datetime import date

# There is currently print commands scattered around the project, 
# Simply to ease the debug process.

# Global variables.
today = date.today()
counter = []

# Pre-define skin / item names and their hash names here.
item_list = {"Chroma 2":"Chroma%202%20Case",
"Chroma 3":"Chroma%203%20Case",
"Clutch":"Clutch%20Case",
"CS20":"CS20%20Case",
"Danger Zone":"Danger%20Zone%20Case",
"Falchion":"Falchion%20Case",
"Fracture":"Fracture%20Case",
"Gamma ":"Gamma%20%20Case",
"Gamma 2":"Gamma%202%20Case",
"Glove":"Glove%20Case",
"Horizon ":"Horizon%20%20Case",
"Huntsman":"Huntsman%20Case",
"Operation Bravo":"Operation%20Bravo%20Case",
"Operation Breakout Weapon":"Operation%20Breakout%20Weapon%20Case",
"Operation Broken Fang":"Operation%20Broken%20Fang%20Case",
"Operation Hydra":"Operation%20Hydra%20Case",
"Operation Phoenix Weapon":"Operation%20Phoenix%20Weapon%20Case",
"Operation Vanguard Weapon":"Operation%20Vanguard%20Weapon%20Case",
"Operation Wildfire":"Operation%20Wildfire%20Case",
"Prisma":"Prisma%20Case",
"Prisma 2":"Prisma%202%20Case",
"Revolver":"Revolver%20Case",
"Shadow":"Shadow%20Case",
"Shattered Web":"Shattered%20Web%20Case",
"Spectrum":"Spectrum%20Case",
"Spectrum 2":"Spectrum%202%20Case",
"Winter Offensive Weapon":"Winter%20Offensive%20Weapon%20Case"}

# Stores the data with a date and time.
datastore = {}

# Call this function as wait(desired time to wait), and format it in seconds.
def wait(timer):
    if timer < 61:
        wait_time = timer
        #print("Waiting for ", wait_time, " seconds")
    else: 
        wait_time = timer / 60
        #print("Waiting for ", wait_time, " minutes.")
    time.sleep(timer)
    #print("Continuing.")

# Store the data.
def database(pulled_data):
    dt = datetime.datetime.now()
    now = dt.strftime("%Y-%m-%d-%H:%M")
    datastore[now] = pulled_data

# Pull the data from Steam "API".
def puller():
    pulled_data = ""
    pulled_items = []
    for item in item_list:
        pulled_items.append(item)
        url = (f"http://steamcommunity.com/market/priceoverview/?appid=730&market_hash_name={item_list[item]}&currency=3")
        pull = requests.get(url)
        data = json.loads(pull.content)
        if data == None:
            print(f"\nError in: json.loads((requests.get(url)).content), datavalue is: {data}")
            print(f"Item: {item}")
            timer = 10
            wait(timer)
        while True:  
          if data == None:
            print(f"Error in: json.loads((requests.get(url)).content), datavalue is: {data}")
            print(f"Item: {item}")
            timer = 5
            wait(timer)
          else: 
            print(f"Pulled {item}")
            break
        item_data = ""
        for point in data:
            if point == "success":
                pass
            else:
                datapoint = f"{point}"
                datapoint = datapoint.replace("_", " ")
                item_data += (f"{datapoint}: {data[point]} ")
        pulled_data += f"\n{item} {item_data}"
    print(f"\nAcquired data for {pulled_items}.")
    database(pulled_data)
            
# Test database.
def print_database():
    with open("backlog.txt", "a", encoding="utf-8") as file:
        for record in datastore:
            backlog = "\n" + record + " " + datastore[record] + "\n"
            file.write(backlog)
            #print(datastore)
    print(f"Data stored to backlog.")

# This console gives the user an ability to interact with the scraper.
def userconsole():
    print("Console is open! Simply type a command.")
    while True:
        user = input("")
        commandNotFoundError = "... didn't recognise the command. Try 'help'?\n"
        commands_list = ["help", "create", "create backlog", "exit", "status", "clear"]
        commands = ""
        for command in commands_list:
            commands += command
        
        sentence = user.split(" ")
        
        if user in commands_list:
            if user == "help":
                print(commands)
            
            elif "create" in sentence:
                if user == "create backlog":
                    print_database()
                else:
                    print("Usage: 'create' [object] \nAvialable objects: 'backlog.'") 
            elif user == "exit":
                print("Are you sure you want to exit the program?\nThis stops the data collection entirely.\n")
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
            elif user == "status":
                pullcount = 0
                for i in counter:
                    pullcount += 1        
                print(f"Pullcount: {pullcount}")
            elif user == "clear":
                print("\n" * 50)
        else:
            print(commandNotFoundError)
def loop():
    while True:
        counter.append(1)
        puller()
        # print(f"Data received for desired items.\nStoring data...")
        timer = 120
        wait(timer)

def main():
    mainthread = threading.Thread(target=loop)
    mainthread.start()
    userconsole()

if __name__ =="__main__":
    main()
