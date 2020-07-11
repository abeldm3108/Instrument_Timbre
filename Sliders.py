from matplotlib.widgets import Slider  # import the Slider widget
import numpy as np
import matplotlib.pyplot as plt
from music import * 

armonics = [0,0,0,0,0,0,0,0]

slider_min = 0    # the minimial value of the paramater a
slider_max = 1   # the maximal value of the paramater a
slider_init = 0   # the value of the parameter a to be used initially, when the graph is created

def update(a):
    armonics[a]=
    #sin_plot.set_ydata(np.sin(a*x)) # set new y-coordinates of the plotted points
    #fig.canvas.draw_idle()          # redraw the plot

class ArmonicSlider:
    '''
    slider_1_plt = plt.axes([0.15, 0., 0.8, 0.05]) #Left margin / bottom margin / widht / height

    # here we create the slider
    slider_1 = Slider(slider_1_plt,      # the axes object containing the slider
                    '1st armonic',  # the name of the slider parameter
                    slider_min,          # minimal value of the parameter
                    slider_max,          # maximal value of the parameter
                    valinit=slider_init  # initial value of the parameter
                    )
    '''
    slider_plt = []
    slider = []
    for i in range(4):
        slider_plt.append(plt.axes([0.15, 0.9-0.1*i, 0.8, 0.05]))
        slider.append(Slider(slider_plt[i], " armonic", slider_min, slider_max, valinit=slider_init))
        slider[i].on_changed(update)

# Next we define a function that will be executed each time the value
# indicated by the slider changes. The variable of this function will
# be assigned the value of the slider.


# the final step is to specify that the slider needs to
# execute the above function when its value changes
#a_slider.on_changed(update)



playnote(hz=220, , time=10, intensity = 0.3)

plt.show()
