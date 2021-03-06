from tkinter import *
from playfrequency import *
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
#slider_val = np.empty(numberofharmonics, DoubleVar())

#Creating update function of sliders
def updatelabelinfo1(val):
   harmonic[0]=slider1_val.get()
   labelvar.set(str(slider1_val.get())+"   " +str(slider2_val.get())+"   " +str(slider3_val.get()))
   sd.stop()
   playnote(freq=freq_def, duration=maxtime, instrument=harmonic, intensity=1,loop=True)
def updatelabelinfo2(val):
   harmonic[1]=slider2_val.get()
   labelvar.set(str(slider1_val.get())+"   " +str(slider2_val.get())+"   " +str(slider3_val.get()))
   sd.stop()
   playnote(freq=freq_def, duration=maxtime, instrument=harmonic, intensity=1,loop=True)
def updatelabelinfo3(val):
   harmonic[2]=slider3_val.get()
   labelvar.set(str(slider1_val.get())+"   " +str(slider2_val.get())+"   " +str(slider3_val.get()))
   sd.stop()
   playnote(freq=freq_def, duration=maxtime, instrument=harmonic, intensity=1,loop=True)

#Creating sliders
slider1_val=DoubleVar()
slider2_val=DoubleVar()
slider3_val=DoubleVar()
slider1 = Scale(root, label="Harmonic 1",variable=slider1_val, tickinterval=0.25 , from_=sliderminval, to=slidermaxval, length=sliderlength, width= sliderwidth, command=updatelabelinfo1)
slider1.pack(side=LEFT)
slider1.set(5)
slider2 = Scale(root, label="Harmonic 2",variable=slider2_val, from_=sliderminval, to=slidermaxval, length=sliderlength, width= sliderwidth, command=updatelabelinfo2)
slider2.pack(side=LEFT)
slider2.set(5)
slider3 = Scale(root, label="Harmonic 3", variable=slider3_val, from_=sliderminval, to=slidermaxval, length=sliderlength, width= sliderwidth, command=updatelabelinfo3)
slider3.pack(side=LEFT)
slider3.set(5)


'''
for i in range(numberofharmonics):
    def updateharmonic[i](val):
        harmonic[i]=val
'''
def updatelabelinfo1(i, val):
   label.config(text = str(val)+" in slider number "+str(i))

labelvar=StringVar()
label = Label(root,textvariable=labelvar)
label.pack()

'''
for i in range(numberofharmonics):
    namefunction="updatelabelinfo"+str(i)
    slider.append(Scale(root,label = str(i), from_=sliderminval, to=slidermaxval,length=sliderlength, width=sliderwidth, command=updatelabelinfo(i,3)))
    slider[i].pack(side=LEFT)
    harmonic[i]=slider[i].get()
'''

root.mainloop()

