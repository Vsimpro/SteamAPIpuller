import scraper_server
from scraper import datastore
from scraper import print_database
from scraper import counter

# Global variables
commands_list = ["help", "create", "create backlog", "exit", "status", "clear", "server", "server start", "server stop"]

# Messages.
def commandOpenMsg():
    print("Console is open! Simply type a command.")
def commandNotFound():
    print("... didn't recognise the command. Try 'help'?")
def areYouSureMSG():
    print("Are you sure you want to exit the program?\nThis stops the data collection entirely.\n")

def commandlist():
    commands = ""
    for command in commands_list:
        commands += command
    print(commands, "\n")

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

def server_command(user):
    if user == "server start":
        scraper_server.main()
    elif user == "server stop":
        scraper_server.stop()
    else:
        print("Usage: 'server' [start / stop]")

def main(user):
    sentence = user.split(" ")
    if user in commands_list:
        if user == "help":
            commandlist()    

        elif "create" in sentence:
            print("This pops.")
            create(user)

        elif "server" in sentence:
            print("not yet implemented.")
            server_command(user)
        
        elif user == "status":
            pullCount()
            
        elif user == "clear":
            print("\n" * 50)
            
    else:
        commandNotFound()