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
plt.savefig('compareLinearQuadraditic_day2.pgf',format='pgf')


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
plt.savefig('compareQuadraditicCubic_day2.pgf',format='pgf')
