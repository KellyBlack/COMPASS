#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import sys


sys.path.insert(0, '../')
from BasicPlot import BasicPlot

plotter = BasicPlot()

###############################
plotter.clearPlot()

fig = plotter.setFigure(None,(8, 4),80,'w','k')
plotter.clearPlot()
plotter.setupGrid(0.3,'--',
                  0.0,1.0,7.1,
                  -2.0,0.5,2.1)
plotter.setAxesBounds(0.9,7.1,-2.1,2.1)
plotter.axesDecorations('Sequence of Numbers','n','Value')

ax = plt.gca()
ax.set_aspect(0.5)
#plt.show()
plt.savefig('reviewSequence_week2Day1.pgf',format='pgf')


###############################
plotter.clearPlot()

plotter.setFigure(fig.number,(8, 4),80,'w','k')
fig.set_figheight(6.0)
fig.set_figwidth(8.0)


def f(t):
    return((t/2.0)**2.0+2.0)
     
a = 1.0
b = 5.0

t = np.arange(0.0,6.0,0.1)
plotter.addFunction(t,f(t),'k-',2.0)
plotter.xAxisTicks([a,b],['a','b'],'horizontal')
plotter.yAxisTicks([f(a),f(b)],['f(a)','f(b)'],'horizontal')
plotter.setAxesBounds(0.0,6.0,0.0,12.0)

plotter.markJumps([[a,f(a),True],[b,f(b),True],
        ],8.0)

#plt.show()
plt.savefig('averageRateChange_week2Day1.pgf',format='pgf')

