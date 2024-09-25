#My Attempt

import sys
import os
from pathlib import Path
from PIL import Image

#to change the directory in the terminal window: Set-Location -Path "file path name"
#Set-Location -Path "C:\Users\elysia.kilayko\OneDrive\Documents\VS Code\Learning\Python\ZTM\pokedex"

# currentDirectory = os.path.dirname(__file__)
# os.chdir(currentDirectory)
# print(currentDirectory)

#grab the first and second argument (\Pokedex and \new), which are inputted in the terminal window
#full input into the terminal window: python JPGtoPNGConverter2.py Pokedex New

jpgLocation = sys.argv[1]
pngLocation = sys.argv[2]

# check if new exists, if not create a new one
# checks if both the path and directory exists
if os.path.exists(pngLocation) and os.path.isdir(pngLocation):
    print("New folder already exists")
else:
    print("New folder does not exist, will create one now")
    newFolder = pngLocation
    os.mkdir(newFolder)

p = Path("./Pokedex")
jpg_files = list(p.glob("**/*.jpg"))
print(jpg_files)

#loop through Pokedex and convert images to png, and save them to the new folder
for img in os.listdir(jpgLocation):
    jpgPath = os.path.join(jpgLocation,img) #get the location of the jpg file
    picture = Image.open(jpgPath) #need to load the image
    pokemon = os.path.splitext(img)[0] #get the pokemon name
    pngPath = os.path.join(pngLocation, f"{pokemon}.png") #create location for png file
    picture.save(pngPath)

