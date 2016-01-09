#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import sys


sys.path.insert(0, '../')
from BasicPlot import BasicPlot

plotter = BasicPlot()




###############################
plotter.clearPlot()

plotter.subplot(2,1,1)
plotter.addFunction([0,1],[1,1],'k-',2.0)
plotter.addFunction([1,2],[0,0],'k-',2.0)
plotter.addFunction([2,3],[-1,-1],'k-',2.0)
plotter.addFunction([3,4],[0,0],'k-',2.0)
plotter.markJumps([[0,1,False],[1,1,True],
                   [1,0,False],[2,0,True],
                   [2,-1,False],[3,-1,True],
                   [3,0,False],[4,0,True],
                   ],8.0)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,4.1,
                  -1.0,1.0,1.1)
plotter.setAxesBounds(-0.1,4.1,-1.1,1.1)
plotter.axesDecorations('Velocity of an Object','','Velocity (m/s)')

plotter.subplot(2,1,2)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,4.1,
                  -1.5,0.5,1.6)
plotter.setAxesBounds(-0.1,4.1,-1.6,1.6)
plotter.axesDecorations('Position of an Object','time (sec)','Position (m)')

#plt.show()
plt.savefig('preclass_week3day1.pgf',format='pgf')

###############################
plotter.clearPlot()

plotter.subplot(2,1,1)
plotter.addFunction([0,1],[0,1],'k-',2.0)
plotter.addFunction([1,2],[1,0],'k-',2.0)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,2.1,
                  -1.0,1.0,1.1)
plotter.setAxesBounds(-0.1,2.1,-1.1,1.1)
plotter.axesDecorations('Velocity of an Object','','Velocity (m/s)')

plotter.subplot(2,1,2)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,4.1,
                  -2.5,1.0,2.6)
plotter.setAxesBounds(-0.1,2.1,-2.6,2.6)
plotter.axesDecorations('Position of an Object','time (sec)','Position (m)')

#plt.show()
plt.savefig('preclassTwo_week3day1.pgf',format='pgf')


###############################
plotter.clearPlot()

plotter.subplot(2,1,1)
plotter.addFunction([0,1],[1,1],'k-',2.0)
plotter.addFunction([1,2],[-1,-1],'k-',2.0)
plotter.markJumps([[0,1,False],[1,1,True],
                   [1,-1,False],[2,-1,True]],8.0)
plotter.setupGrid(0.3,'--',
                  0.0,0.5,2.1,
                  -1.0,0.5,1.1)
plotter.setAxesBounds(-0.1,2.1,-1.1,1.1)
plotter.axesDecorations('Velocity of an Object','','Velocity (m/s)')

plotter.subplot(2,1,2)
plotter.setupGrid(0.3,'--',
                  0.0,0.5,2.1,
                  -1.5,0.5,1.6)
plotter.setAxesBounds(-0.1,2.1,-1.6,1.6)
plotter.axesDecorations('Position of an Object','time (sec)','Position (m)')

#plt.show()
plt.savefig('localMaxPiecewiseConstVel_week3day1.pgf',format='pgf')

###############################
plotter.clearPlot()

plotter.subplot(2,1,1)
plotter.addFunction([0,1],[-1,-1],'k-',2.0)
plotter.addFunction([1,2],[1,1],'k-',2.0)
plotter.markJumps([[0,-1,False],[1,-1,True],
                   [1,1,False],[2,1,True]],8.0)
plotter.setupGrid(0.3,'--',
                  0.0,0.5,2.1,
                  -1.0,0.5,1.1)
plotter.setAxesBounds(-0.1,2.1,-1.1,1.1)
plotter.axesDecorations('Velocity of an Object','','Velocity (m/s)')

plotter.subplot(2,1,2)
plotter.setupGrid(0.3,'--',
                  0.0,0.5,2.1,
                  -1.5,0.5,1.6)
plotter.setAxesBounds(-0.1,2.1,-1.6,1.6)
plotter.axesDecorations('Position of an Object','time (sec)','Position (m)')

#plt.show()
plt.savefig('localMaxPiecewiseConstVelTwo_week3day1.pgf',format='pgf')


###############################
plotter.clearPlot()

plotter.subplot(2,1,1)
plotter.addFunction([0,2],[-1,1],'k-',2.0)
plotter.setupGrid(0.3,'--',
                  0.0,0.5,2.1,
                  -1.0,0.5,1.1)
plotter.setAxesBounds(-0.1,2.1,-1.1,1.1)
plotter.axesDecorations('Velocity of an Object','','Velocity (m/s)')

plotter.subplot(2,1,2)
plotter.setupGrid(0.3,'--',
                  0.0,0.5,2.1,
                  -1.5,0.5,1.6)
plotter.setAxesBounds(-0.1,2.1,-1.6,1.6)
plotter.axesDecorations('Position of an Object','time (sec)','Position (m)')

#plt.show()
plt.savefig('localMaxPiecewiseConstVelThree_week3day1.pgf',format='pgf')

###############################
plotter.clearPlot()

plotter.setupGrid(0.3,'--',
                  -2.0,0.5,2.1,
                  -2.0,0.5,2.1)
plotter.setAxesBounds(-2.1,2.1,-2.1,2.1)
plotter.axesDecorations('Optimization','x','y')

#plt.show()
plt.savefig('constrainedOptimizationOne.pgf',format='pgf')


