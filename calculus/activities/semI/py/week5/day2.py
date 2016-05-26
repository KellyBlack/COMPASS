#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path
from matplotlib.patches import FancyArrowPatch
from matplotlib.patches import Ellipse
import math

import sys


sys.path.insert(0, '../')
from BasicPlot import BasicPlot

plotter = BasicPlot()

###############################
plotter.clearPlot()

plotter.setAxes(True)
axis = plotter.getAxes()
t = np.arange(0.0,3.0,0.1)
#plotter.addFunction(t,np.exp(t),'k-',2.0)

plotter.setAxesBounds(0.0,3.0,-20.0,20.0)
plotter.setupGrid(0.3,'--',
                  -0.0,1.0,3.1,
                   -20.0,5.0,20.1)
plotter.axesDecorations('Position of an Object','t (s)','x (m)')


plt.draw()
#plt.show()
plt.savefig('logarithm_week5day2.pgf',format='pgf')



