#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import sys


sys.path.insert(0, '../')
from BasicPlot import BasicPlot

plotter = BasicPlot()

# Make the plot for the velocity
plotter.subplot(2,1,1)

with plt.xkcd():
    plotter.addFunction([0,1],[ -1, -1], 'k-',2.0)
    plotter.addFunction([1,2],[ 0 ,0], 'k-',2.0)
    plotter.addFunction([2,3],[ 2 ,2], 'k-',2.0)
    plotter.addFunction([3,4],[ 1, 1], 'k-',2.0)
    plotter.markJumps([[0,-1,False],[1,-1,True],
                       [1,0,False],[2,0,True],
                       [2,2,False],[3,2,True],
                       [3,1,False],[4,1,True],
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
                  -1.0,1.0,6.1)
plotter.setAxesBounds(-0.1,4.1,-1.1,6.1)
plotter.axesDecorations('Position of an Object','Time (sec)','Position (m)')

#plt.show()
plt.savefig('vel2Pos_HW1.pgf',format='pgf')






# Make the plot for the velocity
plotter.clearPlot()
plotter.subplot(2,1,1)

plotter.setupGrid(0.3,'--',
    0.0,1.0,4.1,
    -2.0,1.0,4.1)
plotter.setAxesBounds(-0.1,4.1,-2.6,4.1)
plotter.axesDecorations('Velocity of an Object','','Velocity (m/s)')

## make the empty plot for the distance
plotter.subplot(2,1,2)

with plt.xkcd():
    plotter.addFunction([0,1,2,3,4],[1,0,-2,1,0], 'k-',2.0)

plotter.setupGrid(0.3,'--',
                  0.0,1.0,4.1,
                  -2.0,0.5,1.1)
plotter.setAxesBounds(-0.1,4.1,-2.1,1.1)
plotter.axesDecorations('Position of an Object','Time (sec)','Position (m)')

#plt.show()
plt.savefig('pos2Vel_HW1.pgf',format='pgf')


