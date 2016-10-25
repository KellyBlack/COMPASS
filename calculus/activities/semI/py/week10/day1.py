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

plotter.setAxes(False)
axis = plotter.getAxes()

plotter.setAxesBounds(-0.1,2.1,-0.1,2.1)

axis.add_patch(Polygon(np.array([[0.0,1.0],[1.0,1.0],[1.0,1.8]]),edgecolor='black',facecolor='none'))
plotter.addFunction([0.9,0.9,1.0],[1.0,1.1,1.1],'k-',1.0)
plotter.placeText(0.12,1.02,r'$\pi/3$',fontsize=14)
plotter.placeText(0.90,1.34,r'$0.6$',fontsize=14)
#plotter.placeText(0.45,1.7,r'$0.4$',fontsize=14)
plotter.placeText(0.02,1.7,'A',fontsize=20)

#axis.add_patch(Polygon(np.array([[1.1,1.0],[2.0,1.0],[2.0,2.0]]),edgecolor='black',facecolor='none'))
#plotter.addFunction([1.9,1.9,2.0],[1.0,1.1,1.1],'k-',1.0)
#plotter.placeText(1.22,1.02,r'$\pi/6$',fontsize=14)
#plotter.placeText(1.90,1.34,r'$0.5$',fontsize=14)
##plotter.placeText(0.45,0.7,r'$0.4$',fontsize=14)
#plotter.placeText(1.06,1.7,'B',fontsize=20)

#axis.add_patch(Polygon(np.array([[0.0,0.0],[1.0,0.0],[1.0,0.9]]),edgecolor='black',facecolor='none'))
#plotter.addFunction([0.9,0.9,1.0],[0.0,0.1,0.1],'k-',1.0)
#plotter.placeText(0.12,0.02,r'$\theta$',fontsize=14)
#plotter.placeText(0.90,0.34,r'$0.4$',fontsize=14)
#plotter.placeText(0.45,0.5,r'$0.6$',fontsize=14)
#plotter.placeText(0.02,0.7,'C',fontsize=20)


#axis.add_patch(Polygon(np.array([[1.1,0.0],[2.0,0.0],[2.0,0.7]]),edgecolor='black',facecolor='none'))
#plotter.addFunction([1.9,1.9,2.0],[0.0,0.1,0.1],'k-',1.0)
#plotter.placeText(1.22,0.02,r'$\theta$',fontsize=14)
#plotter.placeText(1.52,0.02,r'$0.3$',fontsize=14)
#plotter.placeText(1.45,0.4,r'$0.6$',fontsize=14)
#plotter.placeText(1.06,0.7,'D',fontsize=20)

axis.add_patch(Polygon(np.array([[0.1,0.0],[1.0,0.0],[1.0,0.7]]),edgecolor='black',facecolor='none'))
plotter.addFunction([0.9,0.9,1.0],[0.0,0.1,0.1],'k-',1.0)
plotter.placeText(0.22,0.02,r'$\theta$',fontsize=14)
plotter.placeText(0.52,0.02,r'$0.3$',fontsize=14)
plotter.placeText(0.45,0.4,r'$0.6$',fontsize=14)
plotter.placeText(0.06,0.7,'B',fontsize=20)



#plotter.setupGrid(0.3,'--',
#                   0.0,1.0,4.1,
#                  -1.0,1.0,16.1)
#plotter.axesDecorations('Nonconstant Force','Time (sec)','Force (N)')


plt.draw()
#plt.show()
plt.savefig('simpleWedge.pgf',format='pgf')

