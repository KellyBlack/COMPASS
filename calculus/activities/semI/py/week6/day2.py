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

plotter.subplot(2,1,1)

plotter.setAxesBounds(0.0,2.0*np.pi,-1.1,1.1)
plotter.setupGrid(0.3,'--',
                  -0.0,np.pi*0.5,2.0*np.pi+.01,
                   -1.0,0.5,1.1)
plotter.xAxisTicks([0.0,np.pi*0.5,np.pi,np.pi*1.5,np.pi*2.0],
                   ["0",r"$\frac{\pi}{2}$",r"$\pi$",r"$\frac{3\pi}{2}$",r"$2\pi$"])
plotter.axesDecorations('Velocity of an Object','','v (m/sec)')


plotter.subplot(2,1,2)

t = np.linspace(0.0,2.0*np.pi,40)
plotter.addFunction(t,np.sin(t),'k-',2.0)

plotter.setAxesBounds(0.0,2.0*np.pi,-1.1,1.1)
plotter.setupGrid(0.3,'--',
                  -0.0,np.pi*0.5,2.0*np.pi+.01,
                   -1.0,0.5,1.1)
plotter.xAxisTicks([0.0,np.pi*0.5,np.pi,np.pi*1.5,np.pi*2.0],
                   ["0",r"$\frac{\pi}{2}$",r"$\pi$",r"$\frac{3\pi}{2}$",r"$2\pi$"])
plotter.axesDecorations('Position of an Object','t (s)','x (m)')


plt.draw()
#plt.show()
plt.savefig('sineInTime_week6day2.pgf',format='pgf')

###############################
plotter.clearPlot()

plotter.setAxes(True)
axis = plotter.getAxes()

plotter.subplot(2,1,1)

plotter.setAxesBounds(0.0,2.0*np.pi,-1.1,1.1)
t = np.linspace(0.0,2.0*np.pi,40)
plotter.addFunction(t,np.sin(t),'k-',2.0)
plotter.setupGrid(0.3,'--',
                  -0.0,np.pi*0.5,2.0*np.pi+.01,
                   -1.0,0.5,1.1)
plotter.xAxisTicks([0.0,np.pi*0.5,np.pi,np.pi*1.5,np.pi*2.0],
                   ["0",r"$\frac{\pi}{2}$",r"$\pi$",r"$\frac{3\pi}{2}$",r"$2\pi$"])
plotter.axesDecorations('Velocity of an Object','','v (m/sec)')


plotter.subplot(2,1,2)

plotter.setAxesBounds(0.0,2.0*np.pi,-1.1,1.1)
plotter.setupGrid(0.3,'--',
                  -0.0,np.pi*0.5,2.0*np.pi+.01,
                   -1.0,0.5,1.1)
plotter.xAxisTicks([0.0,np.pi*0.5,np.pi,np.pi*1.5,np.pi*2.0],
                   ["0",r"$\frac{\pi}{2}$",r"$\pi$",r"$\frac{3\pi}{2}$",r"$2\pi$"])
plotter.axesDecorations('Position of an Object','t (s)','x (m)')


plt.draw()
#plt.show()
plt.savefig('sineInTimeVel_week6day2.pgf',format='pgf')



