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

plotter = BasicPlot()


###############################
plotter.clearPlot()

plt.rc('text', usetex=True)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,7.1,
                  -1.0,0.2,1.1)
plotter.setAxesBounds(-0.1,7.1,-1.1,1.1)
plotter.axesDecorations(r'Sequence','n','a_n')



plt.draw()
#plt.show()
plt.savefig('firstSequenceAxes.pgf',format='pgf')

