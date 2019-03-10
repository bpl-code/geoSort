#geoSort.py
#Sorts a folder of pictures based on their location data

from GPSPhoto import gpsphoto
import os

fileName = 'IMG_6952.jpg'
print(gpsphoto.getGPSData(fileName))

os.mkdir('news folder') #creates new folder


#Choose file directory 
#Choose naming convension (LATER FEATURE FOR DONT ASK)

def chooseDirectory():
    directory = input("Enter Directory: ")
    return 0

def 