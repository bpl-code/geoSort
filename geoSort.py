#geoSort.py
#Sorts a folder of pictures, based on their location data, into new folders

from GPSPhoto import gpsphoto
import os
from geopy.geocoders import Nominatim
from glob import glob



class session():
    def __init__ (self, directory="./", folders=[], folderConfig='ccd'):
        self.directory = directory
        self.folders = folders

        self.topTier = ''
        self.midTier = ''
        self.bottomTier = ''

        self.topFolders = [] 
        self.midFolders = [] 
        self.bottomFolders = [] 

        self.folderConfig = folderConfig
        self.sessionPhotos = []

        if self.folderConfig == "ccd":
            self.setTiers(".getCountry()", ".getCity()", ".getDate()")

    def setDirectory(self, newDirectory):
        self.directory = newDirectory

    def setTopTiers(self, command):
        self.topTier = command

    def setMidTier(self, command):
        self.midTier = command
    
    def setBottomTier(self, command):
        self.bottomTier = command

    def setTiers(self, top, mid, bottom):
        self.setTopTiers(top)
        self.setMidTier(mid)
        self.setBottomTier(bottom)

    def setFolders(self, topFolders, midFolders, bottomFolders):
        self.topFolders = topFolders
        self.midFolders = midFolders
        self.bottomFolders = bottomFolders


    def setSessionPhotos(self, photos):
        self.sessionPhotos = photos

    def getDirectory(self):
        return self.directory

    def getFolderConfig(self):
        return self.folderConfig

    def getFolders(self):
        return self.topFolders, self.midFolders, self.bottomFolders

    def getFirstFolders(self):
        return self.topFolders

    def getSecondFolders(self):
        return self.midFolders

    def getThirdFolders(self):
        return self.bottomFolders

    def getTopTier(self):
        return self.topTier

    def getMidTier(self):
        return self.midTier
    
    def getBottomTier(self):
        return self.bottomTier

    def getSessionPhotos(self):
        return self.sessionPhotos


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
        self.suburb = self.findSuburb()
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

    def findSuburb(self):
        gpsData = gpsphoto.getGPSData(self.photoURL)
        suburb = gpsData['Date'] #change to the correct suburb key
        return suburb

    def findDate(self):
        gpsData = gpsphoto.getGPSData(self.photoURL) 
        date = gpsData['Date']
        date = date.split('/')
        date = '-'.join(date)
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

    def getSuburb(self):
        return self.suburb

    def getDate(self):
        return self.date

    def getTime(self):
        return self.time

    def getEventName(self):
        return self.eventName


def loadConfigFile(directory='./'):
    try: 
        configFile = open(directory + ".configFile.txt", "r")
        previousSession = configFile.readline()
        print("Config File found! Loading now...")
        print(previousSession)
        print("Session loaded.")
        loadedSession = eval(previousSession)
        configFile.close()
        return loadedSession
    except: 
        print("No configFile exists: New Session created.")
        newSession = session(directory=directory)
        return newSession
    

def writeToConfigFile(session):
    configFile = open(session.getDirectory() + ".configFile.txt", 'w')
    configFile.write("session(directory='{}', folders={}, folderConfig='{}')".format(session.getDirectory(), session.getFolders(), session.getFolderConfig()))
    configFile.close()


def createPhotoFile(fileURL):
    newPhotoFile = photo(fileURL)
    return newPhotoFile
    

def getFolderTiers(session):

    firstTierFolders = set(session.getFirstFolders())
    secondTierFolders = set(session.getSecondFolders())
    thirdTierFolders = set(session.getThirdFolders())

    topConfigFunction = "photo" + session.getTopTier()
    midConfigFunction = "photo" + session.getMidTier()
    bottomConfigFunction = "photo" + session.getBottomTier()

    for photo in session.getSessionPhotos():
        first = session.getDirectory() + eval(topConfigFunction) 
        second = first + '/' + eval(midConfigFunction) 
        third = second + '/' + eval(bottomConfigFunction)
        firstTierFolders.add(first)
        secondTierFolders.add(second)
        thirdTierFolders.add(third)
    
    session.setFolders(firstTierFolders, secondTierFolders, thirdTierFolders)


def createNewFolders(folderList):
    folderList = locationList
    for folder in folderList:
        try:
            createFolder(location)
        except FileExistsError: 
            pass

def createFolder(folderName, directory="./"):
    os.makedirs(directory + folderName)

def moveFiles(photo, targetLocation):
    #move file to new location
    photoURL = photo
    os.rename(photo, targetLocation)


#Main funciton calls


def startSession(directory):
    session = loadConfigFile(directory=directory)
    return session

def createPhotos(session):
    photos = []
    for jpgs in glob(session.getDirectory() + "*.jpg"):
        photos.append(createPhotoFile(jpgs))

    session.setSessionPhotos(photos)

def createFolders(session):

    getFolderTiers(session)

    firstTier, secondTier, thirdTier = session.getFolders()

    for folder in firstTier:
        try:
            createFolder(folder, directory=session.getDirectory())

        except FileExistsError:
            pass
    
    for folder in secondTier:
        try:
            createFolder(folder, directory=session.getDirectory())

        except FileExistsError:
            pass

    for folder in thirdTier:
        try:
            createFolder(folder, directory=session.getDirectory())

        except FileExistsError:
            pass


def accessTiers(session):
    firstTierFolders = set(session.getFirstFolders())
    secondTierFolders = set(session.getSecondFolders())
    thirdTierFolders = set(session.getThirdFolders())

    firstConfigFunction = "photo" + session.getTopTier()
    secondConfigFunction = "photo" + session.getMidTier()
    thirdConfigFunction = "photo" + session.getBottomTier()

    return (firstConfigFunction, secondConfigFunction, thirdConfigFunction), (firstTierFolders, secondTierFolders, thirdTierFolders)


    
def organiseFiles(session):

    #checks if the country, city and date all match if so moves the file to that location

    tierCalls, folders = accessTiers(session)
    firstTierCall, seondTierCall, thirdTierCall = tierCalls
    thirdTierFolders = folders[2]

    photos = session.getSessionPhotos()

    for photo in photos:
        photoFirstTier = eval(firstTierCall)
        photoSecondTier = eval(seondTierCall)
        photoThirdTier = eval(thirdTierCall)

        for folder in thirdTierFolders:
            if photoFirstTier in folder:
                if photoSecondTier in folder:
                    if photoThirdTier in folder:
                        fileName = folder + '/' + photo.getTime() + '.jpg' #add another photo.get for a more top level address
                        moveFiles(photo.getPhotoURL(), fileName)
        

        


def main():
    return 0 

if __name__ == "__main__":
    main()