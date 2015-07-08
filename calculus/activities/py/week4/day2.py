#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path
from matplotlib.patches import FancyArrowPatch
from matplotlib.patches import Ellipse

import sys


sys.path.insert(0, '../')
from BasicPlot import BasicPlot

plotter = BasicPlot()
fig = plotter.setFigure(None,(8.0, 4.0),80,'w','k')



###############################
plotter.clearPlot()

plotter.setAxes(False)
axis = plotter.getAxes()
plotter.setAxesBounds(0.0,9.0,0.0,6.0)
plotter.addFunction([1.0,8.0,8.0,1.0],[1.0,1.0,5.0,1.0],'k-',2.0)
plotter.addFunction([7.5,7.5,8.0],[1.0,2.0,2.0],'k-',1.0)
plotter.placeText(1.9,1.1,r'$\theta$',fontsize=18)
plotter.placeText(7.5,4.0,r'$\psi$',fontsize=18)
plotter.placeText(4.1,0.3,r'5.0',fontsize=18)
plotter.placeText(8.2,2.5,r'2.0',fontsize=18)
#axis.set_aspect(4.0/8.0)

plt.draw()
#plt.show()
plt.savefig('preClassTriangle1_week4day2.pgf',format='pgf')

###############################
plotter.clearPlot()
fig = plotter.setFigure(None,(4.0, 8.0),80,'w','k')

plotter.setAxes(False)
axis = plotter.getAxes()
plotter.setAxesBounds(0.0,5.0,0.0,10.0)
plotter.addFunction([1.0,4.0,4.0,1.0],[1.0,1.0,10.0,1.0],'k-',2.0)
plotter.addFunction([3.5,3.5,4.0],[1.0,1.7,1.7],'k-',1.0)
plotter.placeText(1.2,1.1,r'$\theta$',fontsize=18)
plotter.placeText(3.5,8.0,r'$\psi$',fontsize=18)
plotter.placeText(2.5,0.5,r'5.0',fontsize=18)
plotter.placeText(4.25,4.5,r'2.0',fontsize=18)
#axis.set_aspect(2.0)

plt.draw()
#plt.show()
plt.savefig('preClassTriangle2_week4day2.pgf',format='pgf')



###############################
plotter.clearPlot()

fig = plotter.setFigure(None,(8.0, 4.0),80,'w','k')
plotter.setAxes(False)
axis = plotter.getAxes()
plotter.setAxesBounds(0.0,9.0,0.0,6.0)

axis.add_patch(patches.Rectangle((4.5,3.2),1.0,0.5,angle=33.0,fill=True,edgecolor="black",
                                 linewidth=2.0,linestyle='solid',facecolor='black'))
triangle = path.Path(np.array([[0.5,0.5],[8.0,0.5],[8.0,5.5],[0.5,0.5]]),
                codes=np.array([path.Path.MOVETO,path.Path.LINETO,path.Path.LINETO,path.Path.LINETO]),
                closed=True
                )
axis.add_patch(patches.PathPatch(triangle,edgecolor='black',facecolor='white'))
plotter.addFunction([7.5,7.5,8.0],[0.5,1.0,1.0],'k-',1.0)
plotter.placeText(1.3,0.60,r'$\theta$',fontsize=24)
plotter.placeText(7.5,4.7,r'$\psi$',fontsize=24)
#axis.set_aspect(4.0/8.0)

plt.draw()
#plt.show()
plt.savefig('freeBodyDiagram_week4day2.pgf',format='pgf')



###############################
plotter.clearPlot()

plotter.setAxes(False)
axis = plotter.getAxes()
plotter.setAxesBounds(0.0,9.0,0.0,6.0)
triangle = path.Path(np.array([[0.5,0.5],[8.0,0.5],[8.0,5.5],[0.5,0.5]]),
                codes=np.array([path.Path.MOVETO,path.Path.LINETO,path.Path.LINETO,path.Path.LINETO]),
                closed=True
                )
axis.add_patch(patches.PathPatch(triangle,edgecolor='black',facecolor='white'))
plotter.addFunction([7.5,7.5,8.0],[0.5,1.0,1.0],'k-',1.0)
plotter.placeText(1.3,0.6,r'$\theta$',fontsize=24)
plotter.placeText(3.7,0.05,r'$x$',fontsize=24)
plotter.placeText(8.5,2.25,r'$y$',fontsize=24)
plotter.placeText(3.7,3.25,r'$r$',fontsize=24)
#axis.set_aspect(4.0/8.0)

plt.draw()
#plt.show()
plt.savefig('generalRightTriangle_week4day2.pgf',format='pgf')


