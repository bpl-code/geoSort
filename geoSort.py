#geoSort.py
#Sorts a folder of pictures, based on their location data, into new folders

from GPSPhoto import gpsphoto
import os
from geopy.geocoders import Nominatim


class photo():

    def __init__ (self, photoFile):
        self.photoFile = photoFile
        self.latitude, self.longitude, self.coordinates = self.findLatitudeAndLongitude()
        self.fullAddress = self.findFullAddress()
        self.city = self.findCity()
        self.country = self.findCountry()
        self.geolocator = Nominatim(user_agent="geoSort")
        self.fullLocationDetials = geolocator.reverse(loc, addressdetails=True, language='en-GB')
        self.rawAddress = fullLocationDetials.raw


    def findLatitudeAndLongitude(self):
        gpsData = gpsphoto.getGPSData('IMG_5386.jpg') #needs to be replaced with file
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


#os.mkdir('a folder') #creates new folder

def main():
    pic = photo('file')
    print(pic.getCity())

if __name__ == "__main__":
    main()