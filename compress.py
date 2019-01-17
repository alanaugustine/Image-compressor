import PIL
from PIL import Image
import os
import string
dir_name=input("Please input the directory path")
final_dir=input("Enter te final directory path")
width=input("Please enter the final image width")
height=input("Please enter the final image height")
for filename in os.listdir(dir_name):
	img = Image.open(dir_name+'\\'+filename)	
	img=img.resize((width, height),PIL.Image.ANTIALIAS)
	filename=final_dir+'\\'+filename
	img.save(filename,quality=99)
