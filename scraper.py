import requests
import json
import datetime
from datetime import date 


# Date's 
today = date.today()
dt = datetime.datetime.now()
now = dt.strftime("%Y-%m-%d-%H:%M")

# Pre-define case names and their hash names.
case_dictionary = {"Prisma":"Prisma%20Case",
"Prisma2":"Prisma%202%20Case", "Revolver": "Revolver%20Case","Danger Zone":"Danger%20Zone%20Case",
"Horizon Case":"Horizon%20Case"}

# Store the data with a date and time.
datastore = {}

# Pull the data from Steam "API".
def puller():
    print()
    print(today, "\n")
    pulled_data = ""
    for case in case_dictionary:
        case_data = ""
        url = (f"http://steamcommunity.com/market/priceoverview/?appid=730&market_hash_name={case_dictionary[case]}&currency=3")
        pull = requests.get(url)
        data = json.loads(pull.content)
        for point in data:
            if point == "success":
                pass
            else:
                datapoint = f"{point}"
                datapoint = datapoint.replace("_", " ")
                case_data += (f"{datapoint}: {data[point]} ")
        pulled_data += f"\n{case}\n{case_data}"
    database(pulled_data)
            
# Store the data.
def database(pulled_data):
    pull = ""
    pull += pulled_data
    datastore[now] = pull
    pass

# Test database.
def print_database():
    print(datastore)
    #for record in datastore:
    #    print(record," ",datastore[record])
    #pass


puller()
print_database()