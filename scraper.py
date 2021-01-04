import requests
import json
import datetime
from datetime import date 


# Date's 
today = date.today()
dt = datetime.datetime.now()
now = dt.strftime("%Y-%m-%d-%H:%M")

# Pre-define skin / item names and their hash names.
item_list = {"Prisma":"Prisma%20Case",
"Prisma2":"Prisma%202%20Case", "Revolver": "Revolver%20Case","Danger Zone":"Danger%20Zone%20Case",
"Horizon Case":"Horizon%20Case"}

# Store the data with a date and time.
datastore = {}

# Pull the data from Steam "API".
def puller():
    pulled_data = ""
    for item in item_list:
        item_data = ""
        url = (f"http://steamcommunity.com/market/priceoverview/?appid=730&market_hash_name={item_list[item]}&currency=3")
        pull = requests.get(url)
        data = json.loads(pull.content)
        for point in data:
            if point == "success":
                pass
            else:
                datapoint = f"{point}"
                datapoint = datapoint.replace("_", " ")
                item_data += (f"{datapoint}: {data[point]} ")
        pulled_data += f"\n{item}\n{item_data}"
    database(pulled_data)
            
# Store the data.
def database(pulled_data):
    datastore[now] = pulled_data
    pass

# Test database.
def print_database():
    print(datastore)

puller()
