#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import sys


sys.path.insert(0, '../')
from BasicPlot import BasicPlot

plotter = BasicPlot()

###############################
plotter.clearPlot()

# Make the plot for the velocity
plotter.subplot(2,1,1)

t1 = np.arange(0,4.05,0.1)
t2 = np.arange(4,5.01,0.02)
with plt.xkcd():
    plotter.addInterpolant([[0,2.0],[1,0.0],[2.0,-2],
                            [3.0,0.0],[4,2.0]],t1,'k-',2.0)
    plotter.addInterpolant([[4,-1.0],[4.5,0.0],[4.5,0.0],
                            [5.0,-1.0]],t2,'k-',2.0)

    plotter.markJumps([[0,2,True],[4,2,True],
                       [4,-1,False],[5,-1,True],
        ],8.0)
    plotter.setupGrid(0.3,'--',
                      0.0,1.0,5.1,
                      -2.0,1.0,2.1)
    plotter.setAxesBounds(-0.1,5.1,-2.1,2.1)
    plotter.axesDecorations('Velocity of an Object','','Velocity (m/s)')

## make the empty plot for the distance
plotter.subplot(2,1,2)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,5.1,
                  -4.0,1.0,4.1)
plotter.setAxesBounds(-0.1,5.1,-4.1,4.1)
plotter.axesDecorations('Position of an Object','Time (sec)','Position (m)')

#plt.show()
plt.savefig('vel2Pos_introDerivLimit.pgf',format='pgf')

###############################
plotter.clearPlot()

def f(t):
    return(-7/6.0*(t)**3.0+24.0/6.0*t*t-11.0/6.0*t)

t = np.arange(0.0,6.0,0.1)
plotter.addFunction(t,f(t),'k-',2.0)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,3.1,
                  -2.0,0.5,4.1)
plotter.setAxesBounds(0.0,3.1,-2.1,4.1)
plotter.axesDecorations('Position of an Object','time (sec)','Position  (m/sec)')

#plt.show()
plt.savefig('sketchSlope_week2Day2.pgf',format='pgf')


###############################
plotter.clearPlot()

# Make the plot for the velocity
plotter.subplot(2,1,1)

with plt.xkcd():
    plotter.addFunction([0,1],[ 2 ,2], 'k-',2.0)
    plotter.addFunction([1,2],[ 1 ,1], 'k-',2.0)
    plotter.addFunction([2,3],[ 0 ,0], 'k-',2.0)
    plotter.addFunction([3,4],[-1,-1], 'k-',2.0)
    plotter.markJumps([[0,2,False],[1,2,True],
                       [1,1,False],[2,1,True],
                       [2,0,False],[3,0,True],
                       [3,-1,False],[4,-1,True],
        ],8.0)
    plotter.setupGrid(0.3,'--',
                      0.0,1.0,4.1,
                      -1.0,1.0,2.1)
    plotter.setAxesBounds(-0.1,4.1,-1.1,2.1)
    plotter.axesDecorations('Velocity of an Object','','Velocity (m/s)')

## make the empty plot for the distance
plotter.subplot(2,1,2)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,4.1,
                  -1.0,1.0,4.1)
plotter.setAxesBounds(-0.1,4.1,-1.1,4.1)
plotter.axesDecorations('Position of an Object','Time (sec)','Position (m)')

#plt.show()
plt.savefig('vel2Pos_week2day2.pgf',format='pgf')


