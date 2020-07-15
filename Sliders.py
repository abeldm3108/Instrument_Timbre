from tkinter import *
from music import *
import numpy as np

root = Tk()
sliderminval,slidermaxval=0,10
sliderlength, sliderwidth=200,20

harmonic = np.zeros(10)


slider=[]
var =[]

label = Label(root)
label.pack()

def sel():
   selection =var.get()
   label.config(text = selection)

for i in range(10):
    var.append(DoubleVar())
    slider.append(Scale(root, from_=sliderminval, to=slidermaxval,length=sliderlength, width=sliderwidth, variable=var[i]))
    slider[i].pack(side=LEFT)
    harmonic[i]=var[i].get()

label = Label(root,text=var[1].get())
label.pack()

#button = Button(root, text="Play note", command=playnote)

root.geometry("300x300")
root.mainloop()

print(harmonic[1])

