from tkinter import *
from playfrecuency import *
import numpy as np
import sounddevice as sd

root = Tk()
root.geometry("300x300")
sliderminval,slidermaxval=0,10
sliderlength, sliderwidth=200,20
numberofharmonics = 3
maxtime=10
fr_def = 44100
freq_def=220

#Array of intensity of harmonics
harmonic = np.zeros(numberofharmonics)

slider=[]
var =[]

label = Label(root)
label.pack()


#Creating update function of sliders
def updatelabelinfo1(val):
   harmonic[0]=val
   sd.stop()
   playnote(freq=freq_def, duration=maxtime, instrument=harmonic, intensity=1, fr=fr_def)
def updatelabelinfo2(val):
   harmonic[1]=val
   sd.stop()
   playnote(freq=freq_def, duration=maxtime, instrument=harmonic, intensity=1, fr=fr_def)
def updatelabelinfo3(val):
   harmonic[2]=val
   sd.stop()
   playnote(freq=freq_def, duration=maxtime, instrument=harmonic, intensity=1, fr=fr_def)

#Creating sliders
slider1 = Scale(root, label="Harmonic 1", from_=sliderminval, to=slidermaxval, length=sliderlength, width= sliderwidth, command=updatelabelinfo1).pack(side=LEFT)
slider2 = Scale(root, label="Harmonic 2", from_=sliderminval, to=slidermaxval, length=sliderlength, width= sliderwidth, command=updatelabelinfo2).pack(side=LEFT)
slider3 = Scale(root, label="Harmonic 3", from_=sliderminval, to=slidermaxval, length=sliderlength, width= sliderwidth, command=updatelabelinfo3).pack(side=LEFT)


'''
for i in range(numberofharmonics):
    def updateharmonic[i](val):
        harmonic[i]=val
'''
def updatelabelinfo1(i, val):
   label.config(text = str(val)+" in slider number "+str(i))

label = Label(root,text=0)
label.pack()

'''
for i in range(numberofharmonics):
    namefunction="updatelabelinfo"+str(i)
    slider.append(Scale(root,label = str(i), from_=sliderminval, to=slidermaxval,length=sliderlength, width=sliderwidth, command=updatelabelinfo(i,3)))
    slider[i].pack(side=LEFT)
    harmonic[i]=slider[i].get()
'''

root.mainloop()

