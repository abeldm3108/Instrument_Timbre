from playfrequency import *


playnote(freq=220, instrument=horn2, intensity = 1.5, loop=True)

i=0
while i<10:
    if input()=="stop":
        sd.stop()
        playnote(freq=110, instrument=horn1, intensity = 1.5, duration=3)
        break
    time.sleep(1)
    i=i+1

j=0
while j<3:
    time.sleep(1)
    j=j+1


