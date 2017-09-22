#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path
from matplotlib.patches import FancyArrowPatch
from matplotlib.patches import Ellipse
import math as math

import sys


sys.path.insert(0, '../')
from BasicPlot import BasicPlot

plotter = BasicPlot()
#fig = plotter.setFigure(None,(8.0, 8.0),80,'w','k')


###############################
plotter.clearPlot()
#fig = plotter.setFigure(None,(8.0, 8.0),80,'w','k')

plotter.setAxes(False)
axis = plotter.getAxes()
plotter.setAxesBounds(-10.0,10.0,-10.0,10.0)

axis.add_patch(Ellipse((0.0,0.0),18.2,18.2,edgecolor='black',facecolor='none'))
triangle = path.Path(np.array([[0.0,0.0],[7.5,0.0],[7.5,5.0],[0.0,0.0]]),
                codes=np.array([path.Path.MOVETO,path.Path.LINETO,path.Path.LINETO,path.Path.LINETO]),
                closed=True
                )
axis.add_patch(patches.PathPatch(triangle,edgecolor='black',facecolor='white'))

plotter.addFunction([7.0,7.0,7.5],[0.0,0.5,0.5],'k-',1.0)
plotter.addFunction([-10.0,10.0],[0.0,0.0],'k--',1.0)
plotter.addFunction([0.0,0.0],[-10.0,10.0],'k--',1.0)
plotter.placeText(1.75,0.3,   r'$\theta$',fontsize=24)
plotter.placeText(3.2,-1.05,  r'$x$',fontsize=24)
plotter.placeText(7.95,1.75,  r'$y$',fontsize=24)
plotter.placeText(3.7,3.75,   r'$r$',fontsize=24)
plotter.placeText(9.5,-1.05,  r'$r$',fontsize=24)
plotter.placeText(-0.95,9.5,  r'$r$',fontsize=24)
plotter.placeText(-11.2,-1.05,r'$-r$',fontsize=24)
plotter.placeText(-1.7,-10.5, r'$-r$',fontsize=24)

axis.add_patch(Ellipse((7.5,5.0),0.5,0.5,edgecolor='black',facecolor='black'))
axis.add_patch(Ellipse((7.32,5.23),0.2,0.2,edgecolor='black',facecolor='black'))
for i in range(4):
    plotter.addFunction([7.5,7.5+0.7*math.cos(2.0*math.pi*(0.05+float(i)/16.0))],
                        [5.0,5.0+0.7*math.sin(2.0*math.pi*(0.05+float(i)/16.0))],'k-',1.0)
    plotter.addFunction([7.5,7.5+0.7*math.cos(2.0*math.pi*(0.55+float(i)/16.0))],
                        [5.0,5.0+0.7*math.sin(2.0*math.pi*(0.55+float(i)/16.0))],'k-',1.0)


axis.set_aspect(1.0)

plt.draw()
#plt.show()
plt.savefig('unitCircleBug_week4day2.pgf',format='pgf')


###############################
plotter.clearPlot()
#fig = plotter.setFigure(None,(8.0, 8.0),80,'w','k')

plotter.setAxes(False)
axis = plotter.getAxes()
plotter.setAxesBounds(-10.0,10.0,-10.0,10.0)

axis.add_patch(Ellipse((0.0,0.0),18.2,18.2,edgecolor='black',facecolor='none'))
triangle = path.Path(np.array([[0.0,0.0],[7.5,0.0],[7.5,5.0],[0.0,0.0]]),
                codes=np.array([path.Path.MOVETO,path.Path.LINETO,path.Path.LINETO,path.Path.LINETO]),
                closed=True
                )
axis.add_patch(patches.PathPatch(triangle,edgecolor='black',facecolor='white'))
plotter.addFunction([7.0,7.0,7.5],[0.0,0.5,0.5],'k-',1.0)
plotter.addFunction([-10.0,10.0],[0.0,0.0],'k--',1.0)
plotter.addFunction([0.0,0.0],[-10.0,10.0],'k--',1.0)
plotter.placeText(1.75,0.3,   r'$\theta$',fontsize=24)
plotter.placeText(3.2,-1.05,  r'$x$',fontsize=24)
plotter.placeText(7.95,1.75,  r'$y$',fontsize=24)
plotter.placeText(3.7,3.75,   r'$r$',fontsize=24)
plotter.placeText(9.5,-1.05,  r'$1$',fontsize=24)
plotter.placeText(-0.95,9.5,  r'$1$',fontsize=24)
plotter.placeText(-11.2,-1.05,r'$-1$',fontsize=24)
plotter.placeText(-1.7,-10.5, r'$-1$',fontsize=24)

axis.set_aspect(1.0)

plt.draw()
#plt.show()
plt.savefig('unitCircle_week4day2.pgf',format='pgf')

