from playfrequency import playnote
import numpy as np
import sounddevice as sd

MAXTIME = 10

harmonic = np.zeros(9)

def lbl_1_Clicked(i):
    harmonic[0]=i
    sd.stop()
    playnote(duration=MAXTIME, instrument=harmonic, intensity=1,loop=True)

def lbl_2_Clicked(i):
    harmonic[1]=i
    sd.stop()
    playnote(duration=MAXTIME, instrument=harmonic, intensity=1,loop=True)

def lbl_3_Clicked(i):
    harmonic[2]=i
    sd.stop()
    playnote(duration=MAXTIME, instrument=harmonic, intensity=1,loop=True)

def lbl_4_Clicked(i):
    harmonic[3]=i
    sd.stop()
    playnote(duration=MAXTIME, instrument=harmonic, intensity=1,loop=True)

def lbl_5_Clicked(i):
    harmonic[4]=i
    sd.stop()
    playnote(duration=MAXTIME, instrument=harmonic, intensity=1,loop=True)

def lbl_6_Clicked(i):
    harmonic[5]=i
    sd.stop()
    playnote(duration=MAXTIME, instrument=harmonic, intensity=1,loop=True)

def lbl_7_Clicked(i):
    harmonic[6]=i
    sd.stop()
    playnote(duration=MAXTIME, instrument=harmonic, intensity=1,loop=True)

def lbl_8_Clicked(i):
    harmonic[7]=i
    sd.stop()
    playnote(duration=MAXTIME, instrument=harmonic, intensity=1,loop=True)

def lbl_9_Clicked(i):
    harmonic[8]=i
    sd.stop()
    playnote(duration=MAXTIME, instrument=harmonic, intensity=1,loop=True)
