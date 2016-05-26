#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import sys


sys.path.insert(0, '../')
from BasicPlot import BasicPlot

plotter = BasicPlot()


#t = np.arange(0.0,2.0,0.1)
#plotter.addFunction(t,t,'k-',2.0)
#plotter.addFunction(t,t^2,'k-',2.0)

plotter.setupGrid(0.3,'--',
                  0.0,0.5,2.1,
                  0.0,1.0,5.1)

plotter.setAxesBounds(0.0,2.0,0.0,5.0)
plotter.axesDecorations('Position of an Object','Time (sec)','Position (m)')

#plt.show()
plt.savefig('compareLinearQuadraditic_day3.pgf',format='pgf')


###############################
plotter.clearPlot()
#t = np.arange(0.0,2.0,0.1)
#plotter.addFunction(t,t,'k-',2.0)
#plotter.addFunction(t,t^2,'k-',2.0)

plotter.setupGrid(0.3,'--',
                  0.0,1.0,4.1,
                  0.0,10.0,70.1)

plotter.setAxesBounds(0.0,4.0,0.0,70.0)
plotter.axesDecorations('Position of an Object','Time (sec)','Position (m)')

#plt.show()
plt.savefig('compareQuadraditicCubic_day3.pgf',format='pgf')


###############################
plotter.clearPlot()
t = np.arange(0.0,4.0,0.1)
plotter.addFunction(t,t**2,'k-',2.0)

def pos(t):
    return(t*t)

plotter.markJumps([[3.0,pos(3.0),True],[2.5,pos(2.5),True],
                   [2.0,pos(2.0),True],[1.0,pos(1.0),True],
                   [2.75,pos(2.75),True]
        ],8.0)

plotter.setupGrid(0.3,'--',
                  0.0,1.0,4.1,
                  0.0,4.0,16.1)

plotter.setAxesBounds(0.0,4.0,0.0,16.0)
plotter.axesDecorations('Position of an Object','Time (sec)','Position (m)')

#plt.show()
plt.savefig('averageRateChange_day3.pgf',format='pgf')


###############################
plotter.clearPlot()

plotter.setFigure(None,(8, 4),80,'w','k')
plotter.clearPlot()
plotter.setupGrid(0.3,'--',
                  1.0,1.0,7.1,
                  0.0,1.0,9.1)
plotter.setAxesBounds(0.9,7.1,-0.1,9.1)
plotter.axesDecorations('Sequence of Numbers','n','Value')

ax = plt.gca()
ax.set_aspect(0.25)
#plt.show()
plt.savefig('averageRateChangeSequence_day3.pgf',format='pgf')
