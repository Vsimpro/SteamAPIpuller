#! python3 scraper.py

import requests
import json
import datetime
import time
import threading
from datetime import date

# There is currently print commands scattered around the project, 
# Simply to ease the debug process.

# Global variables.
today = date.today()

# Pre-define skin / item names and their hash names here.
item_list = {"Prisma":"Prisma%20Case",
"Prisma2":"Prisma%202%20Case", "Revolver": "Revolver%20Case","Danger Zone":"Danger%20Zone%20Case",
"Horizon Case":"Horizon%20Case"}

# Stores the data with a date and time.
datastore = {}

# Call this function as wait(desired time to wait), and format it in seconds.
def wait(timer):
    if timer < 61:
        wait_time = timer
        print("Waiting for ", wait_time, " seconds")
    else:
        wait_time = time / 60
        print("Waiting for ", wait_time, " minutes.")
    time.sleep(timer)
    print("Continuing.")

# Store the data.
def database(pulled_data):
    dt = datetime.datetime.now()
    now = dt.strftime("%Y-%m-%d-%H:%M")
    datastore[now] = pulled_data

    pass

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
            timer = 5
            print()
            wait(timer)
            puller()
        else: 
            pass
        item_data = ""
        for point in data:
            if point == "success":
                pass
            else:
                datapoint = f"{point}"
                datapoint = datapoint.replace("_", " ")
                item_data += (f"{datapoint}: {data[point]} ")
        pulled_data += f"\n{item}\n{item_data}"
    print(f"\nAcquired data for {pulled_items}.")
    database(pulled_data)
            
# Test database.
def print_database():
    with open("backlog.txt", "a", encoding="utf-8") as file:
        for record in datastore:
            backlog = "\n" + record + " " + datastore[record] + "\n"
            file.write(backlog)
            print(datastore)
    print(f"Data stored to backlog.")

# This console gives the user an ability to interact with the scraper.
def userconsole():
    while True:
        user = input("Console is open! Simply type a command.\n")
        commands ="Avialable commands: " + "\n" "help" + "\n" + "create" + "\n"
        sentence = user.split(" ")
        if user == "help":
            print(commands)
        elif user == "Help":
            print(commands)
            userconsole()
        elif "create" in sentence:
            if "backlog" in sentence:
                print_database()
                pass
            else:
                print("Usage: 'create' [what you want to create.] \nAvialable objects: 'backlog.'")
            pass 
        else:
            print("... didn't recognise the command. Try 'help'?\n")
    
def loop():
    while True:
        puller()
        # print(f"Data received for desired items.\nStoring data...")
        timer = 60
        wait(timer)

def main():
    mainthread = threading.Thread(target=loop)
    mainthread.start()
    userconsole()

if __name__ =="__main__":
    main()
