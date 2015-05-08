#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from BasicPlot import BasicPlot

def f(t):
    return((t/2.0)**2.0+2.0)
     
plotter = BasicPlot()

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
plt.savefig('averageRateChange_day1.pgf',format='pgf')
