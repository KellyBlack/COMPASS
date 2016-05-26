#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.insert(0, '../')
from BasicPlot import BasicPlot


#plt.xkcd(randomness=0.1)
#with plt.xkcd():

# Make the first plot
plotter = BasicPlot()
plotter.addFunction([0,1,2,3],[0,1,1,2], 'k-',2.0)
plotter.setupGrid(0.5,'--',
                  0.0,0.5,3.0,
                  0.0,0.25,2.5)
plotter.axesDecorations('Position of an Object','Time (sec)','Position (m)')
#plt.text(1.0,3.025, r'$\alpha=100,\ \sigma=15$')
plt.savefig('preClass1.pgf')
#plt.show()


# Make the second plot
plotter.clearPlot()
plotter.addFunction([0,1,2,3],[0,0.5,3,2], 'k-',2.0)
plotter.setupGrid(0.5,'--',
                  0.0,0.5,3.0,
                  0.0,0.2,3.0,)
plotter.axesDecorations('Position of an Object','Time (sec)','Position (m)')
#plt.text(1.0,3.025, r'$\alpha=100,\ \sigma=15$')
plt.savefig('preClass2.pgf')
#plt.show()


# Make the third plot
plotter.clearPlot()
plotter.addFunction([0,1,2,3],[0,-1.0,2,1], 'k-',2.0)
plotter.setupGrid(0.5,'--',
                  0.0,0.5,3.0,
                  -1.0,0.2,2.0)
plotter.axesDecorations('Position of an Object','Time (sec)','Position (m)')
#plt.text(1.0,3.025, r'$\alpha=100,\ \sigma=15$'
plt.savefig('preClass3.pgf')
#plt.show()
