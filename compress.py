from tkinter import *
import tkinter
from tkinter import messagebox
import os
import PIL
from PIL import Image
import string

def process():
    width=Entry.get(E1)
    height=Entry.get(E2)
    dir_name=Entry.get(E3)
    final_dir=Entry.get(E4)
    width=int(width)
    height=int(height)
    for filename in os.listdir(dir_name):
        img=Image.open(dir_name+'\\'+filename)	
        img=img.resize((width, height),PIL.Image.ANTIALIAS)
        filename=final_dir+'\\'+filename
        img.save(filename,quality=99)
        
        
top = tkinter.Tk()
L1 = Label(top, text="Image compressor",).grid(row=0,column=1)
L2 = Label(top, text="Final width",).grid(row=1,column=0)
L3 = Label(top, text="Final Height",).grid(row=2,column=0)
L4 = Label(top, text="Source Dircetory",).grid(row=3,column=0)
L4 = Label(top, text="Destination Directory",).grid(row=4,column=0)
E1 = Entry(top, bd =5)
E1.grid(row=1,column=1)
E2 = Entry(top, bd =5)
E2.grid(row=2,column=1)
E3 = Entry(top, bd =5)
E3.grid(row=3,column=1)
E4 = Entry(top, bd =5)
E4.grid(row=4,column=1)
B=Button(top, text ="Compress",command = process).grid(row=5,column=1,)

top.mainloop()
