import numpy as np
import sounddevice as sd
import time
from scipy.io.wavfile import write

fr_def = 44100
freq_def = 440.0
duration_def = 5.0

def nor(coe = []): #Normalize the vector
    sum=0
    for i in coe:
        sum = sum + i

    if sum==0:
        return coe
    
    for index, i in enumerate(coe):
        coe[index]=i/sum

    return coe

def pot(dec=[]): #Convert dB to intensity coefficients 
        
        
    for index, item in enumerate(dec):
        if index != 0:
                dec[index]=np.power(np.e, item/10)/np.power(np.e, dec[0]/10)

    dec[0]=1

    return dec

horn1 = pot([15,18,20,17,10,11,10,8])

horn2 = [0.1637, 0.3263, 0.4212, 0.2391, 0.0492, 0.0608, 0.0518, 0.0293, 0.0115, 0.0085, 0.0068, 0.0018, 0.0008, 0.001, 0.0007, 0.0008,]

def playnote(freq=freq_def, duration=duration_def, instrument=[1], intensity=1, fr=fr_def, loop=False, wait=False): #Plays the data of the armonics of instrument vector
    instrument=nor(instrument)
    each_sample_number = np.arange(duration*fr)
    wave=0
    for i, coe in enumerate(instrument):
        wave = wave+intensity*coe*np.sin(2*np.pi*each_sample_number*freq*(i+1)/fr)
    wave=intensity*wave
    if loop:
        sd.play(wave, fr, loop=True)
        if wait:
            sd.wait()
    else:
        sd.play(wave,fr)
        if wait:
            time.sleep(duration)
            sd.wait()

def writenote(name= "sinewave.wav", freq=freq_def, duration=duration_def, instrument=[1], intensity=1, fr=fr_def):  #Creates a WAV file with the data
    instrument=nor(instrument)
    each_sample_number = np.arange(duration*fr)
    wave=0
    for i, coe in enumerate(instrument):
        wave = wave+intensity*coe*np.sin(2*np.pi*each_sample_number*freq*(i+1)/fr)
    wave=intensity*wave
    wave_ints=np.int16(wave*32767)
    write(name, fr, wave_ints)







