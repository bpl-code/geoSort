#gsUI.py
#Terminal Based UI for geoSort 

import geoSort
from glob import glob

#HAve the user enter commands 
#based on the command the program runs the function


#user input:
#open directory
#auto:
#search for config file 
#if none create new session
#user input:
#sort new photos
#show folders
#set naming conventions
#quit


def main(): 

    chooseDirectory()
    session, configFile = createSession()
    saveConfigFile(configFile, str(["Folder1","folder2"]))
    run = True 

    while run:
        userInput = input("Enter a command: ")
        if userInput == "cd":
            chooseDirectory()
        elif userInput == "q":
            run = False


def chooseDirectory():
    userInput = input("Type the directory you wish to use or press '.' for current: ")
    if userInput == ".":
        userInput = "./"
    session.setDirectory(userInput)

def loadConfigFile():
    geoSort.loadConfigFile()
    
def createSession():
    session = geoSort.createSession()
    configFile = geoSort.createConfigFile()
    return session, configFile

def saveConfigFile(configFile, folders):
    geoSort.saveConfigFile(configFile, folders)





if __name__ == "__main__":
    main()