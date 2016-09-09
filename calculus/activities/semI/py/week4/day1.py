#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch
import sys


sys.path.insert(0, '../')
from BasicPlot import BasicPlot

plotter = BasicPlot()





###############################
plotter.clearPlot()

t = np.arange(-2,2,0.1)
plotter.addInterpolant([[-2,-3],[0,2],[1,3],[2,5]],t,'k-',2.0)
plotter.setupGrid(0.3,'--',
                  -2.0,1.0,2.1,
                  -4.0,1.0,5.1)
plotter.setAxesBounds(-2.1,2.1,-3.1,5.1)
plotter.axesDecorations('Position of an Object','Time (s)','Position (m)')

plt.draw()
#plt.show()
plt.savefig('simpleInverse_week4day1.pgf',format='pgf')


###############################
plotter.clearPlot()

t = np.arange(-2,2,0.1)
plotter.addInterpolant([[-2,-3],[0,2],[1,1],[2,5]],t,'k-',2.0)
plotter.setupGrid(0.3,'--',
                  -2.0,1.0,2.1,
                  -4.0,1.0,5.1)
plotter.setAxesBounds(-2.1,2.1,-3.1,5.1)
plotter.axesDecorations('Position of an Object','Time (s)','Position (m)')

plt.draw()
#plt.show()
plt.savefig('simpleNoInverse_week4day1.pgf',format='pgf')


###############################
plotter.clearPlot()

plotter.setAxes(False)
axis = plotter.getAxes()
plotter.setAxesBounds(0.0,10.0,0.0,10.0)
axis.add_patch(patches.Rectangle((2.0,0.5),6.0,8.0,fill=False,edgecolor="black",
                                 linewidth=2.0,linestyle='solid'))
axis.add_patch(patches.Rectangle((8.0,0.5),1.0,8.0,fill=False,edgecolor="black",
                                 linewidth=2.0,linestyle='solid',hatch='\\'))
axis.add_patch(patches.Rectangle((2.0,8.5),6.0,1.0,fill=False,edgecolor="black",
                                 linewidth=2.0,linestyle='solid',hatch='/'))
axis.add_patch(patches.Rectangle((8.0,8.5),1.0,1.0,fill=False,edgecolor="black",
                                 linewidth=2.0,linestyle='solid',hatch='x'))

arrows = FancyArrowPatch(posA=(9.70,8.0), posB=(9.0, 9.1),
                            edgecolor = 'black',facecolor='white',
                            arrowstyle="fancy",
                            mutation_scale=700**.5,
                            connectionstyle="angle3,angleA=90.0,angleB=0.0")
axis.add_patch(arrows)

plotter.placeText(9.2,7.4,r'$A\cap B$',fontsize=22,color='blue')
plotter.placeText(5.2,9.75,'A',fontsize=22,color='red')
plotter.placeText(9.2,4.50,'B',fontsize=22,color='green')

plotter.placeText(2.0,0.0,r'0',fontsize=18)
plotter.placeText(7.6,0.0,r'$g(t)$',fontsize=18)
plotter.placeText(8.7,0.0,r'$g(t+\Delta t)$',fontsize=18)

plotter.placeText(1.5,0.4,r'0',fontsize=18)
plotter.placeText(1.1,8.3,r'$f(t)$',fontsize=18)
plotter.placeText(0.2,9.5,r'$f(t+\Delta t)$',fontsize=18)


plt.draw()
#plt.show()
plt.savefig('boxesTogether_week4day1.pgf',format='pgf')

###############################
plotter.clearPlot()

plotter.setAxes(False)
axis = plotter.getAxes()
plotter.setAxesBounds(0.0,20.0,0.0,10.0)
axis.add_patch(patches.Rectangle((2.0,0.5),6.0,8.0,fill=False,edgecolor="black",
                                 linewidth=2.0,linestyle='solid'))

plotter.placeText(2.0,0.0,r'0',fontsize=18)
plotter.placeText(7.8,0.0,r'$g(t)$',fontsize=18)
plotter.placeText(1.5,0.4,r'0',fontsize=18)
plotter.placeText(0.5,8.5,r'$f(t)$',fontsize=18)

axis.add_patch(patches.Rectangle((12.0,0.5),7.0,9.0,fill=False,edgecolor="black",
                                 linewidth=2.0,linestyle='dashed'))

plotter.placeText(12.0,0.0,r'0',fontsize=18)
plotter.placeText(11.2,0.4,r'0',fontsize=18)
plotter.placeText(18.0,0.0,r'$g(t+\Delta t)$',fontsize=18)
plotter.placeText(8.5,9.25,r'$f(t+\Delta t)$',fontsize=18)

arrows = FancyArrowPatch(posA=(8.5,4.0), posB=(11.5, 4.5),
                            edgecolor = 'black',facecolor='white',
                            arrowstyle="fancy",
                            mutation_scale=700**.5,
                            connectionstyle="arc3")

axis.add_patch(arrows)

plt.draw()
#plt.show()
plt.savefig('boxesSideBySide_week4day1.pgf',format='pgf')


###############################
plotter.clearPlot()

plotter.subplot(1,2,1)
t = np.arange(-2,2.05,0.1)
plotter.addInterpolant([[-2,3],[-1,2],[0,-1],[1,-3],[2,2]],t,'k-',2.0)
plotter.setupGrid(0.3,'--',
                  -2.0,1.0,2.1,
                  -4.0,1.0,4.1)
plotter.setAxesBounds(-2.1,2.1,-3.1,4.1)
plotter.axesDecorations('f','t','Graph of f')

plotter.subplot(1,2,2)
plotter.addInterpolant([[-2,-1],[-1,1],[1,2],[2,3]],t,'k-',2.0)
plotter.setupGrid(0.3,'--',
                  -2.0,1.0,2.1,
                  -4.0,1.0,4.1)
plotter.setAxesBounds(-2.1,2.1,-3.1,4.1)
plotter.axesDecorations('g','t','Graph of g')


#plt.draw()
#plt.show()
plt.savefig('compositionTwoFunctions.pgf',format='pgf')


###############################
plotter.clearPlot()

plotter.subplot(1,2,1)
t = np.arange(-2,2.05,0.1)
plotter.addInterpolant([[-2,-2],[-1,2],[0,3],[1,1],[2,-2]],t,'k-',2.0)
plotter.setupGrid(0.3,'--',
                  -2.0,1.0,2.1,
                  -4.0,1.0,4.1)
plotter.setAxesBounds(-2.1,2.1,-3.1,4.1)
plotter.axesDecorations('f','t','Graph of f')

plotter.subplot(1,2,2)
plotter.addInterpolant([[-2,3],[-1,1],[1,-1],[2,-3]],t,'k-',2.0)
plotter.setupGrid(0.3,'--',
                  -2.0,1.0,2.1,
                  -4.0,1.0,4.1)
plotter.setAxesBounds(-2.1,2.1,-3.1,4.1)
plotter.axesDecorations('g','t','Graph of g')


plt.draw()
#plt.show()
plt.savefig('compositionTwoFunctionsDec.pgf',format='pgf')
