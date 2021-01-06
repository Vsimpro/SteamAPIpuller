from scraper import datastore
from scraper import print_database
from scraper import counter

# Refactored commands here to ease the codeline count in scraper.py
# Scraper.py's command's in command line should always redirect the actions here.
# Only exception being "exit"

# Global variables
commands_list = ["help", "create", "create backlog", "exit", "status", "clear"]

def commandOpenMsg():
    print("Console is open! Simply type a command.")
def commandNotFound():
    
    print("... didn't recognise the command. Try 'help'?")

def commandlist():
    commands = ""
    for command in commands_list:
        commands += command
    print(commands)

def areYouSureMSG():
    print("Are you sure you want to exit the program?\nThis stops the data collection entirely.\n")

def Clear():
    print("\n" * 50)

def pullCount():
    pullcount = 0
    for i in counter:
        pullcount += 1        
    print(f"Pullcount: {pullcount}")

def create(user):
    if user == "create backlog":
        print_database()
        print("Creating..")
    else:
        print("Usage: 'create' [object] \nAvialable objects: 'backlog.'")

def main(user):

    sentence = user.split(" ")
    if user in commands_list:
        if user == "help":
            commandlist()    

        elif "create" in sentence:
            print("This pops.")
            create(user)

        elif user == "status":
            pullCount()

        elif user == "clear":
            Clear()
    else:
        commandNotFound()