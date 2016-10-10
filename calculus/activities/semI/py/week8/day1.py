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

def force(t):
    return(t*t)

###############################
plotter.clearPlot()

plotter.setAxes(True)
axis = plotter.getAxes()

plotter.setAxesBounds(0.0,4.0,-1.0,16.0)
for pos in range(2):
    t = 2.0*float(pos)
    plotter.addFunction([t,t+2.0],[force(t),force(t)],'k-',2.0)
    plotter.markJumps([[t,force(t),False],[t+2.0,force(t),True]],8.0)

plotter.setupGrid(0.3,'--',
                   0.0,1.0,4.1,
                  -1.0,1.0,16.1)
plotter.axesDecorations('Nonconstant Force','Position (m)','Force (N)')


plt.draw()
#plt.show()
plt.savefig('piecewiseConstantForceI_week8day1.pgf',format='pgf')

###############################
plotter.clearPlot()

plotter.setAxes(True)
axis = plotter.getAxes()

plotter.setAxesBounds(0.0,4.0,-1.0,16.0)
for pos in range(4):
    t = float(pos)
    plotter.addFunction([t,t+1.0],[force(t),force(t)],'k-',2.0)
    plotter.markJumps([[t,force(t),False],[t+1.0,force(t),True]],8.0)

plotter.setupGrid(0.3,'--',
                   0.0,1.0,4.1,
                  -1.0,1.0,16.1)
plotter.axesDecorations('Nonconstant Force','Position (m)','Force (N)')


plt.draw()
#plt.show()
plt.savefig('piecewiseConstantForceII_week8day1.pgf',format='pgf')

###############################
plotter.clearPlot()

plotter.setAxes(True)
axis = plotter.getAxes()

plotter.setAxesBounds(0.0,4.0,-1.0,16.0)
for pos in range(4):
    t = float(pos)
    plotter.addFunction([t,t+1.0],[force(t),force(t)],'k-',2.0)
    plotter.markJumps([[t,force(t),False],[t+1.0,force(t),True]],8.0)

plotter.setupGrid(0.3,'--',
                   0.0,1.0,4.1,
                  -1.0,1.0,16.1)
plotter.axesDecorations('Nonconstant Force','Time (s)','Force (N)')


plt.draw()
#plt.show()
plt.savefig('piecewiseConstantForceIII_week8day1.pgf',format='pgf')


###############################
plotter.clearPlot()

plotter.setAxes(True)
axis = plotter.getAxes()

plotter.setAxesBounds(0.0,4.0,-1.0,16.0)
plotter.setupGrid(0.3,'--',
                   0.0,1.0,4.1,
                  -1.0,1.0,16.1)
plotter.axesDecorations('Nonconstant Force','Time (sec)','Force (N)')


plt.draw()
#plt.show()
plt.savefig('changingForceGrid_week8day1.pgf',format='pgf')



