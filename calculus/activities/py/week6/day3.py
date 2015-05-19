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

plotter.setAxesBounds(-5.0,5.0,-5.0,5.0)
plotter.setupGrid(0.3,'--',
                  -5.0,1.0,5.1,
                  -5.0,1.0,5.1)
plotter.axesDecorations('Position','x (m)','y (m)')


plt.draw()
#plt.show()
plt.savefig('trigPath_week6day3.pgf',format='pgf')

###############################
plotter.clearPlot()
#fig = plotter.setFigure(None,(8.0, 8.0),80,'w','k')

axis = plotter.getAxes()
plotter.setAxesBounds(-1.1,1.1,-1.1,1.1)

axis.add_patch(Ellipse((0.0,0.0),2.0,2.0,edgecolor='black',facecolor='none'))
plotter.axesDecorations('Unit Circle','x (m)','y (m)')
plotter.setupGrid(0.3,'--',
                  -1.0,0.5,1.1,
                  -1.0,0.5,1.1)
axis.set_aspect(1.0)

plt.draw()
#plt.show()
plt.savefig('unitCircle_week6day3.pgf',format='pgf')


