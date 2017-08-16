#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import sys


sys.path.insert(0, '../')
from BasicPlot import BasicPlot

def f(t):
    return((t/2.0)**2.0+2.0)
     
plotter = BasicPlot()

# Make the plot for the velocity for the pre-class work
plotter.subplot(1,1,1)

with plt.xkcd():
    plotter.addFunction([0,1],[ 2 ,2], 'k-',2.0)
    plotter.addFunction([1,2],[ -1 ,-1], 'k-',2.0)
    plotter.addFunction([2,3],[ 0 ,0], 'k-',2.0)
    plotter.addFunction([3,4],[1,1], 'k-',2.0)
    plotter.markJumps([[0,2,False],[1,2,True],
                       [1,-1,False],[2,-1,True],
                       [2,0,False],[3,0,True],
                       [3,1,False],[4,1,True],
        ],8.0)
    plotter.setupGrid(0.3,'--',
                      0.0,1.0,4.1,
                      -1.0,1.0,2.1)
    plotter.setAxesBounds(-0.1,4.1,-1.1,2.1)
    plotter.axesDecorations('Velocity of an Object','','Velocity (m/s)')


#plt.show()
plt.savefig('activity2PreClass.pgf',format='pgf')

#exit(0)


# Make the plot for the position

a = 1.0
b = 5.0

t = np.arange(0.0,6.0,0.1)
plotter.addFunction(t,f(t),'k-',2.0)
plotter.xAxisTicks([a,b],['a','b'],'horizontal')
plotter.yAxisTicks([f(a),f(b)],['f(a)','f(b)'],'horizontal')
plotter.setAxesBounds(0.0,6.0,0.0,12.0)

plotter.addFunction([a,a],[0,f(a)],'b:',2.0)
plotter.addFunction([b,b],[0,f(b)],'b:',2.0)

plotter.addFunction([0,b],[f(a),f(a)],'r:',2.0)
plotter.addFunction([0,b],[f(b),f(b)],'r:',2.0)

t1 = np.array([0,6])
plotter.addFunction(t1,(t1-a)*(f(b)-f(a))/(b-a)+f(a),'k--',2.0)

plotter.placeText((a+b)/2,f(a)-0.5,r"$b-a$",fontsize=18)
plotter.placeText(b,(f(a)+f(b))/2,r"$f(b)-f(a)$",fontsize=18)
plotter.placeText(a,f(b)+2.0,r"slope=$\frac{f(b)-f(a)}{b-a}$",fontsize=18)

plotter.axesDecorations('Position of an Object','Time (sec)','Position (m)')

#plt.show()
plt.savefig('averageRateChange_day2.pgf',format='pgf')


plotter.clearPlot()
plotter.subplot(2,1,1)
plotter.setupGrid(0.3,'--',
                  0.0,0.5,2.1,
                  -3.0,1.0,7.1)
plotter.setAxesBounds(-0.1,2.1,-3.1,3.1)
plotter.axesDecorations('Velocity of an Object','','Velocity (m/s)')

plotter.subplot(2,1,2)
plotter.setupGrid(0.3,'--',
                  0.0,0.5,2.1,
                  -2.0,1.0,2.1)
plotter.setAxesBounds(-0.1,2.1,-2.1,2.1)
plotter.axesDecorations('Position of an Object','Time (sec)','Position (m)')

#plt.show()
plt.savefig('table1graph_day2.pgf',format='pgf')


plotter.clearPlot()
plotter.subplot(2,1,1)
plotter.setupGrid(0.3,'--',
                  0.0,0.5,2.1,
                  -3.0,1.0,7.1)
plotter.setAxesBounds(-0.1,2.1,-3.1,7.1)
plotter.axesDecorations('Velocity of an Object','','Velocity (m/s)')

plotter.subplot(2,1,2)
plotter.setupGrid(0.3,'--',
                  0.0,0.5,2.1,
                  -2.0,1.0,2.1)
plotter.setAxesBounds(-0.1,2.1,-2.1,2.1)
plotter.axesDecorations('Position of an Object','Time (sec)','Position (m)')

#plt.show()
plt.savefig('table2graph_day2.pgf',format='pgf')


plotter.clearPlot()

def vel(t):
    return(t*(t-3)*(t-5)/(1*(1-3)*(1-5)) - 2*t*(t-1)*(t-5)/(3*(3-1)*(3-5)) + 0*t*(t-1)*(t-3)/(5*(5-1)*(5-3)))

t = np.arange(0.0,6.0,0.1)
plotter.addFunction(t,vel(t),'b-',2.0)
#plotter.markJumps([[1.0,vel(1.0),True],[2.0,vel(2.0),True],
#                   [2.5,vel(2.5),True],[2.75,vel(2.75),True],
#                   [3,vel(3),True],
#        ],8.0)

for pos in [1.0,2.0,2.5,2.75,3.0]:
    plotter.markJumps([[pos,vel(pos),True]],8.0)
    plotter.addFunction(np.array([pos,pos]),np.array([-3.1,vel(pos)]),'k:',1.0)

plotter.setupGrid(0.3,'--',
                  0.0,1.0,6.1,
                  -3.0,0.5,3.1)
plotter.setAxesBounds(-0.1,6.1,-3.1,3.1)
plotter.axesDecorations('Position of an Object','Time (sec)','Position (m)')

#plt.show()
plt.savefig('estimateAvgRateChange_day2.pgf',format='pgf')

plotter.clearPlot()

t = np.arange(0.0,6.0,0.1)
plotter.addFunction(t,vel(t),'b-',2.0)
#plotter.markJumps([[1.0,vel(1.0),True],[2.0,vel(2.0),True],
#                   [2.5,vel(2.5),True],[2.75,vel(2.75),True],
#                   [3,vel(3),True],
#        ],8.0)

plotter.setupGrid(0.3,'--',
                  0.0,1.0,6.1,
                  -3.0,0.5,3.1)
plotter.setAxesBounds(-0.1,6.1,-3.1,3.1)
plotter.axesDecorations('Position of an Object','Time (sec)','Position (m)')

#plt.show()
plt.savefig('estimateAvgRateChangeNeg_day2.pgf',format='pgf')

plotter.setFigure(None,(8, 2),80,'w','k')
plotter.clearPlot()
plotter.setupGrid(0.3,'--',
                  1.0,1.0,7.1,
                  0.0,0.5,2.6)
plotter.setAxesBounds(0.9,7.1,-0.1,1.1)
plotter.axesDecorations('Sequence of Numbers','n','Value')

ax = plt.gca()
ax.set_aspect(0.9)
#plt.show()
plt.savefig('sequenceOne_day2.pgf',format='pgf')

