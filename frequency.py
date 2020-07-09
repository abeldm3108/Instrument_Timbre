import numpy as np
import simpleaudio as sa

fsdefault = 44100
musicaltimedefault = 60

def pot(dec=[]):
        
        
    for index, item in enumerate(dec):
        if index != 0:
                dec[index]=np.power(np.e, item/10)/np.power(np.e, dec[0]/10)

    dec[0]=1

    return dec

def nor(dec = []):
    for i in dec:
        g=0
        dec[g]=i/dec[0]
        g=g+1
    return dec

class Instrument:

    trompa1 = pot([15,18,20,17,10,11,10,8]) 

    trompa2 = nor([0.1637, 0.3263, 0.4212, 0.2391, 0.0492, 0.0608, 0.0518, 0.0293, 0.0115, 0.0085, 0.0068, 0.0018, 0.0008, 0.001, 0.0007, 0.0008,])   

class Melody:

    work_melody_in = [622.25, 659.26, 0, 440, 554.37, 659.26, 880]
    work_times_in = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6, 0.5]

    work_melody_out = [622.25, 659.26, 0, 880, 659.26, 523.25, 440]
    work_times_out = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6, 0.5]

def play(intensity={440:1}, fs = fsdefault, seconds = 3):  

    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * fs, False)

    # Generate a 440 Hz sine wave
    note = 0
    for i in intensity:
        note = note + intensity[i]*np.sin(i * t * 2 * np.pi)
   
    # Ensure that highest value is in 16-bit range
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    
    # Convert to 16-bit data
    audio = audio.astype(np.int16)

    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, fs)

    # Wait for playback to finish before exiting
    play_obj.wait_done()


def playnote(hz=440.0,coe=[],time=3):
    dicintens = {}
    num=1
    #array.__len__()=coe.__len__()
    for j in coe:
        dicintens[hz*num]=j
        num = num+1
    play(intensity=dicintens, seconds=time)
        
