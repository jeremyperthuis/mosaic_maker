import os, sys
from PIL import Image
from math import *
from mosaic_fonctions import *


print"******************************************************************\n"
print"    _  _ ____ ____ ____ _ ____    _  _ ____ _  _ ____ ____ "
print"    |\/| |  | [__  |__| | |       |\/| |__| |_/  |___ |__/ "
print"    |  | |__| ___] |  | | |___    |  | |  | | \_ |___ |  \  v 1.0\n\n"
print"******************************************************************\n"


path = raw_input("Enter images path : ")
imgliste= os.listdir(path)
print "\n\n>>> file found : "+str(len(imgliste))

src = TestDimensionImages(path,imgliste)	

grid = Choix_Proportions(imgliste)

new_image = Image.new('RGB', (int(grid[0])*src[0], int(grid[1])*src[1]))

x=0
y=0

for file in imgliste :
	adr = path+"/"+str(file)
	image_courrante= Image.open(adr)
	print adr
	new_image.paste(image_courrante,(x,y))
	x+=src[0]
	if x == grid[0]*src[0] :
		x = 0
		y +=src[1]

nom = raw_input("Enter a name : ")+".jpg"	
new_image.save(nom)
print ("\nSaved image !")
