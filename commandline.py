import os
from scraper import database
from scraper import print_database
from scraper import counter

# Refactored commands here to ease the codeline count in scraper.py
# Scraper.py's command's in command line should always redirect the actions here.
# Only exception being "exit"

def commandOpenMsg():
    print("Console is open! Simply type a command.")
def commandNotFound():
    
    print("... didn't recognise the command. Try 'help'?")

def commandlist():
    commands_list = ["help", "create", "create backlog", "exit", "status", "clear"]
    commands = ""
    for command in commands_list:
        commands += command
    print(commands)

def areYouSureMSG():
    print("Are you sure you want to exit the program?\nThis stops the data collection entirely.\n")

def Clear():
    print("\n" * 50)
