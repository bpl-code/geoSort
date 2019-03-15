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

    def __init__ (self, fileURL):

        self.photoURL = fileURL
        self.latitude, self.longitude, self.coordinates = self.findLatitudeAndLongitude()
        self.geolocator = Nominatim(user_agent="geoSort", timeout=3)
        self.fullLocationDetials = self.geolocator.reverse(self.getCoordinates(), addressdetails=True, language='en-GB')
        self.rawAddress = self.fullLocationDetials.raw

        self.fullAddress = self.findFullAddress()
        self.city = self.findCity()
        self.country = self.findCountry()
        self.date = self.findDate()

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
    

def openConfigFile():
    try: 
        configFile = open(".configFile.txt", 'x')

    except FileExistsError:

        configFile = open(".configFile.txt", "w+")

    return configFile

def loadConfigFile(configFile):
    folderList = configFile.readLine()
    namingConvesion = configFile.readline()
    


def saveConfigFile(configFile, folders):
    configFile.write(folders)

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


def updateFolderStructure(photoList, session):
    #create a three tire structure
    countryFolders = set()
    cityFolders = set()
    dateFolders = set()
    for photo in photoList:
        first = session.getDirectory() + photo.getCountry()
        second = first + '/' + photo.getCity()
        third = second + '/' + photo.getDate()
        countryFolders.add(first)
        cityFolders.add(second)
        dateFolders.add(third)
    return countryFolders, cityFolders, dateFolders



def createCCDFolderStructure(photoList, currentStructure):
    #Create Country City Date folder structure
    #use a list of city
    return 0 

def createNewFolders(locationList):
    locationList = locationList
    for location in locationList:
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