import startup
import os
from shutil import copyfile
def printDir(dir):
    for i in range(len(os.listdir(dir))):
        print(f"{i + 1} - {os.listdir(dir)[i].split('.')[0]}")
def manage(dir):
    inp = input("""
1 - Use a config
2 - Add a config
3 - Remove a config
   >""")
    if inp == "1":
        print("Select a config to use:")
        printDir(dir)
        inp = input("   >")
        y = input(f"Are you sure you want to switch to {os.listdir(dir)[int(inp)-1].split('.')[0]}? (y/n)")
        if y.lower() == "y" or y.lower() == "yes":
            print("Copying configuration...")
            copyfile(startup.ritogame + f"cfgs/{os.listdir(dir)[int(inp)-1]}", startup.ritogame + "input.ini")
            print("Done.")
        else:
            print("Exiting...")
    elif inp == "2":
        inp = input("Enter the name of the new config: ")
        print("Copying configuration...")
        copyfile(startup.ritogame + "input.ini", startup.ritogame + f"cfgs/{inp}.ini")
        print("Done.")
    else:
        pass

    
cfgs = startup.ritogame + "cfgs/"
manage(cfgs)
