import os
import shutil

source = input("Enter source folder name : ")
destination = input("Enter destination folder : ")

source = source+"/"
destination = destination+"/"

listofFiles = os.listdir(source)

for file in listofFiles :
    shutil.copy(source+file,destination)

