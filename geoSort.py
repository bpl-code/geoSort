#geoSort.py
#Sorts a folder of pictures, based on their location data, into new folders

from GPSPhoto import gpsphoto
import os
from geopy.geocoders import Nominatim


class photo():

    def __init__ (self, photoFile, fileURL):

        self.photoFile = photoFile
        self.fileURL = fileURL
        self.latitude, self.longitude, self.coordinates = self.findLatitudeAndLongitude()
        self.geolocator = Nominatim(user_agent="geoSort")
        self.fullLocationDetials = self.geolocator.reverse(self.getCoordinates(), addressdetails=True, language='en-GB')
        self.rawAddress = self.fullLocationDetials.raw

        self.fullAddress = self.findFullAddress()
        self.city = self.findCity()
        self.country = self.findCountry()

    def findLatitudeAndLongitude(self):
        gpsData = gpsphoto.getGPSData('IMG_5386.jpg') #needs to be replaced with photoFile
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
        country = self.rawAddress['address']['city']
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
    
    def getCountry():
        return self.country



#Choose file directory 
#Choose naming convension (LATER FEATURE FOR DONT ASK)
#iterate through all files
#extract data from file
#create photo object and save geo and date

#find address and add to photo

#create a sort of locations 


def chooseDirectory():
    directory = input("Enter Directory: ")
    return 0

def loadConfigFile():
    #look for a config file
    #update locations sort list with list from config file
    #if no config file return False and run createConfigFile()
    
    return 0

def saveConfigFile():
    #update config file
    return 0

def createConfigFile():
    return 0

def processPhotoFiles():
    #for:
    #selectFiles()
    #run through all jpegs automatically and create a new photofile for each 
    #createPhotoFile()
    #save them to a list return list
    return 0

def addNewLocations(photoList):
    #run through photos adding any new locations to sort list
    return 

def organiseFiles(photoList, locationList):
    #sort which folder the files need to move to and use moveFile()
    return 0 

def selectFile():
    #select next file and return it
    return 0

def createPhotoFile(file):
    newPhotoFile = 'file'
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
    pic = photo('file', 'File')
    print(pic.getCity())

if __name__ == "__main__":
    main()