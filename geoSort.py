#geoSort.py
#Sorts a folder of pictures, based on their location data, into new folders

from GPSPhoto import gpsphoto
import os
from geopy.geocoders import Nominatim
from glob import glob



class session():
    def __init__ (self, directory="./", folders=[]):
        self.directory = directory
        self.folders = folders

    def getDirectory(self):
        return self.directory

    def setDirectory(self, newDirectory):
        self.directory = newDirectory






class photo():

    def __init__ (self, fileURL, eventName=""):

        self.photoURL = fileURL
        self.latitude, self.longitude, self.coordinates = self.findLatitudeAndLongitude()
        self.geolocator = Nominatim(user_agent="geoSort", timeout=3)
        self.fullLocationDetials = self.geolocator.reverse(self.getCoordinates(), addressdetails=True, language='en-GB')
        self.rawAddress = self.fullLocationDetials.raw

        self.fullAddress = self.findFullAddress()
        self.city = self.findCity()
        self.country = self.findCountry()
        self.date = self.findDate()
        self.time = self.findTime()
        self.eventName = eventName

    def findLatitudeAndLongitude(self):
        gpsData = gpsphoto.getGPSData(self.photoURL) 
        latitude = str(gpsData["Latitude"])
        longitude = str(gpsData['Longitude'])
        coordinates = latitude + "," + longitude

        return latitude, longitude, coordinates

    def findFullAddress(self):
        fullAddress = self.rawAddress['display_name']
        return fullAddress

    def findCity(self):
        city = self.rawAddress['address']['city']
        return city

    def findCountry(self):
        country = self.rawAddress['address']['country']
        return country

    def findDate(self):
        gpsData = gpsphoto.getGPSData(self.photoURL) 
        date = gpsData['Date']
        return date

    def findTime(self):
        gpsData = gpsphoto.getGPSData(self.photoURL) 
        time = gpsData['UTC-Time']
        return time

    def getPhotoURL(self):
        return self.photoURL

    def getCoordinates(self):
        return self.coordinates

    def getLatitude(self):
        return self.latitude

    def getLongitude(self):
        return self.longitude

    def getFullAddress(self):
        return self.fullAddress

    def getCity(self):
        return self.city
    
    def getCountry(self):
        return self.country

    def getDate(self):
        return self.date

    def getTime(self):
        return self.time

    def getEventName(self):
        return self.eventName



#Choose file directory 
#Choose naming convension (LATER FEATURE FOR DONT ASK)
#iterate through all files
#extract data from file
#create photo object and save geo and date

#find address and add to photo

#create a sort of locations 

def createSession():
    newSession = session()
    return newSession

def loadSession(loadedDirectory,loadedFolders):
    newSession = session(directory=loadedDirectory, folders=loadedFolders)
    return newSession

def chooseDirectory(userInput, session):
    session.setDirectory(userInput)
    

#open the file with X this will ensure that the file is not already made 
#if it is made then open the file with R 

#If exsists run the extraction function to get data then close the config file 
#then open it again as a W+ file 

def openConfigFile():
    try: 
        configFile = open(".configFile.txt", 'x')
        return configFile, False

    except FileExistsError:

        configFile = open(".configFile.txt", "r")
        return configFile, True



def loadConfigFile(configFile, exsitingFile):
    if exsitingFile:
        topLayer = configFile.readline()
        topLayer = topLayer.split()
        midLayer = configFile.readline()
        midLayer = midLayer.split()
        bottomLayer = configFile.readline()
        bottomLayer = bottomLayer.split()
        #return into truple
        configFile.close()
        return topLayer, midLayer, bottomLayer 
    else:
        pass

def writeToConfigFile(folders):
    configFile = open(".configFile.txt", "w")
    top = " ".join(folders[0])
    mid = " ".join(folders[1])
    bottom = " ".join(folders[2])
    configFile.write("{}\n{}\n{}\n\n".format(top, mid, bottom))
    configFile.close()






def processPhotoFiles(directory):
    allJpegs = glob(directory + "*.jpg")
    photoFiles = []

    for photo in allJpegs:
        photoFiles.append(createPhotoFile(photo))
    return photoFiles

def createPhotoFile(fileURL):
    newPhotoFile = photo(fileURL)
    return newPhotoFile

def getAllCountries(photoList):
    #run through photos adding any new locations to sort list
    countries = []
    for photo in photoList:
        countries.append(photo.getCountry())
    return countries

def getAllCities(photoList):
    cities = []
    for photo in photoList:
        cities.append(photo.getCity())
    return cities


def createFolderStructure(photoList, session, configFile, topConfig=".getCounty()", midConfig=".getCity()", bottomConfig=".getDate()"):
    #create a three tire structure
    topLayerFolders = set(configFig[0])
    midLayerFolders = set(configFig[1])
    bottomLayerFolders = set(configFig[2])

    topConfigFunction = "photo" + topConfig
    midConfigFunction = "photo" + midConfig
    bottomConfigFunction = "photo" + bottomConfig

    for photo in photoList:
        top = session.getDirectory() + photo.getCountry() #replace with exec(topConfigFunction) 
        mid = first + '/' + photo.getCity() #replace with exec(topConfigFunction)
        bottom = second + '/' + photo.getDate() #replace with exec(topConfigFunction)
        topLayerFolders.add(top)
        midLayerFolders.add(mid)
        bottomLayerFolders.add(bottom)

    #create the folders here
    allFolderLayers = topLayerFolders.add(midLayerFolders)
    allFolderLayers.add(bottomLayerFolders)
    createNewFolders(allFolderLayers)
    
    return topLayerFolders, midLayerFolders, bottomLayerFolders


def createNewFolders(folderList):
    folderList = locationList
    for folder in folderList:
        try:
            createFolder(location)
        except FileExistsError: 
            pass

def createFolder(folderName, directory="./"):
    os.makedirs(directory + folderName)

def moveFiles(photo, targetLocation, directory='./'):
    #move file to new location
    photoURL = photo.getPhotoURL()
    os.rename(directory + photoURL, targetLocation + photoURL)


#os.mkdir('a folder') #creates new folder

def main():
    return 0 

if __name__ == "__main__":
    main()