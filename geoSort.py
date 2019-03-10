#geoSort.py
#Sorts a folder of pictures based on their location data

from GPSPhoto import gpsphoto
import os
from geopy.geocoders import Nominatim


class photo():

    def __init__ (self, location, Latitude, Longitude):
        self.Latitude = Latitude
        self.Longitude = Longitude
        self.city = self.getCity(location)
        self.address = self.getAddress(location)

    def getCity(self):
        return 0




data = gpsphoto.getGPSData('IMG_6952.jpg')
loc = str(data["Latitude"]) + "," + str(data['Longitude'])
print(loc)



geolocator = Nominatim(user_agent="geoSort")
location = geolocator.reverse(loc, language='en-GB')
print(location.address)

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