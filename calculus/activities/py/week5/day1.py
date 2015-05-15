#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path
from matplotlib.patches import FancyArrowPatch
from matplotlib.patches import Ellipse

import sys


sys.path.insert(0, '../')
from BasicPlot import BasicPlot

plotter = BasicPlot()

###############################
plotter.clearPlot()

plotter.setAxes(True)
axis = plotter.getAxes()
plotter.setAxesBounds(-5.0,5.0,-5.0,5.0)
plotter.setupGrid(0.3,'--',
                  -5.0,1.0,5.1,
                  -5.0,1.0,5.1)
plotter.axesDecorations('Position of an Object','x (m)','y (m)')


plt.draw()
#plt.show()
plt.savefig('path_week4day3.pgf',format='pgf')



