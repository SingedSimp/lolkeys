import os
from shutil import copyfile
from sys import exit
ritogame = input("Please enter the location of your Riot Games folder (default C:/Riot Games/)\n>")
if ritogame == "": # Sets default if user did not enter anything.
    ritogame = "C:/Riot Games/"
if ritogame[-1] != "/": # Adds trailing slash.
    ritogame = ritogame + "/"
ritogame = ritogame + "League of Legends/Config/" # Adds League of Legends folder from Riot Games folder.
print("Running sanity checks...")
print("Using", ritogame, "as config directory")
dExists = os.path.isdir(ritogame)
print("Config directory exists:", dExists)
if dExists == False: # Kills program if directory does not exist.
    print("Invalid config directory,", ritogame)
    exit("Invalid config directory.")
if os.path.exists(ritogame + "/cfgs/"): # Checks if custom config directory exists.
    print("Custom configs folder exists.")
else: # If it does not, create it.
    print("Custom configs folder does not exist, creating...")
    os.makedirs(ritogame + "/cfgs/")
    print("Created.")
if os.path.isfile(ritogame + "/cfgs/default.ini"): # Check if default config file exists.
    print("Default config file exists.")
else:
    print("Default config file does not exist, copying current config...")
    copyfile(ritogame + "input.ini", ritogame + "cfgs/default.ini")
    print("Copied.")
