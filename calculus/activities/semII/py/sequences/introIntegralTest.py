#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path
from matplotlib.patches import Polygon
from matplotlib.patches import Ellipse
import math

import sys


sys.path.insert(0, '../')
from BasicPlot import BasicPlot

plotter = BasicPlot(aspectRatio=[7.2,2.2])


###############################
plotter.clearPlot()

plt.rc('text', usetex=True)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,7.1,
                  0.0,0.25,1.1)
plotter.setAxesBounds(-0.1,7.1,-0.1,1.1)
plotter.axesDecorations(r'Terms in Series',r'$n$',r'$\frac{1}{n^2}$')
#ax = plotter.getAxes()
#ax.set_aspect(6.0/7.2)



plt.draw()
#plt.show()
plt.savefig('integralTestIntro.pgf',format='pgf')
