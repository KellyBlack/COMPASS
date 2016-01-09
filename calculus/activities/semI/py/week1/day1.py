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
    plotter.addFunction([0,1],[ 1 ,1], 'k-',2.0)
    plotter.addFunction([1,2],[ 2 ,2], 'k-',2.0)
    plotter.addFunction([2,3],[ 0 ,0], 'k-',2.0)
    plotter.addFunction([3,4],[-1,-1], 'k-',2.0)
    plotter.markJumps([[0,1,False],[1,1,True],
                       [1,2,False],[2,2,True],
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
                  -1.0,1.0,6.1)
plotter.setAxesBounds(-0.1,4.1,-1.1,6.1)
plotter.axesDecorations('Position of an Object','Time (sec)','Position (m)')

#plt.show()
plt.savefig('vel2Pos_day1.pgf',format='pgf')

#plt.savefig('vel2Pos_day1.pdf',format='pdf')
#plt.close()





# Make the plot for the velocity
plotter.clearPlot()
plotter.subplot(2,1,1)

plotter.setupGrid(0.3,'--',
    0.0,1.0,4.1,
    -2.0,1.0,4.1)
plotter.setAxesBounds(-0.1,4.1,-1.6,4.1)
plotter.axesDecorations('Velocity of an Object','','Velocity (m/s)')

## make the empty plot for the distance
plotter.subplot(2,1,2)

with plt.xkcd():
    plotter.addFunction([0,1,3,4],[ 0 ,1,-1,2], 'k-',2.0)

plotter.setupGrid(0.3,'--',
                  0.0,1.0,4.1,
                  -1.0,0.5,2.1)
plotter.setAxesBounds(-0.1,4.1,-1.1,2.1)
plotter.axesDecorations('Position of an Object','Time (sec)','Position (m)')

#plt.show()
plt.savefig('pos2Vel_day1.pgf',format='pgf')

#plt.savefig('vel2Pos_day1.pdf',format='pdf')
#plt.close()


