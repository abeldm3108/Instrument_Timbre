from playfrequency import *

playnote(freq=220, instrument=horn1 , duration=7, intensity = 0.6)
playnote(freq=220, instrument=horn2 , duration=7, intensity = 0.6)

playnote(freq=220, instrument=horn1 , duration=7, intensity = 0.6, loop=True)

i=0
while i<10:
    print(i)
    time.sleep(1)
    i=i+1