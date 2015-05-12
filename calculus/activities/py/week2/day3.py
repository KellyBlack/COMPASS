#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import sys


sys.path.insert(0, '../')
from BasicPlot import BasicPlot

plotter = BasicPlot()




###############################
plotter.clearPlot()

def g(t):
    return(2.0*t**3 - 3.0*t - 1)

t = np.arange(0.0,3.0,0.1)
plotter.addFunction(t,g(t),'k-',2.0)
#plotter.setupGrid(0.3,'--',
#                  0.0,1.0,3.1,
#                  -2.0,0.5,4.1)
#plotter.setAxesBounds(0.0,3.1,-2.1,4.1)
plotter.axesDecorations('Position of an Object','time (sec)','Position  (m/sec)')

plt.show()
#plt.savefig('whichAntiderivative_week2Day2.pgf',format='pgf')

