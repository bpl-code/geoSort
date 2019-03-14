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

    def getDirectory():
        return self.directory

    def setDirectory(newDirectory):
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

    def findLatitudeAndLongitude(self):
        gpsData = gpsphoto.getGPSData(self.photoURL) #needs to be replaced with photoFile
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

    def getFileURL(self):
        return self.fileURL

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
    

def loadConfigFile():
    try: 
        configFile = open(".configFile.txt", 'x')

    except FileExistsError:

        configFile = open(".configFile.txt", "w+")

    return configFile

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

def organiseFiles(photoList, locationList):
    #sort which folder the files need to move to and use moveFile()
    #create folder


    return 0 

def selectFile():
    #select next file and return it
    return 0

def createFolders():
    #create new folder from sort list 
    #save new folder to config file
    return 0 

def moveFiles(file, targetLocation):
    #move file to new location
    return

#os.mkdir('a folder') #creates new folder

def main():
    return 0 

if __name__ == "__main__":
    main()