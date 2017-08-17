#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import sys



sys.path.insert(0, '../')
from BasicPlot import BasicPlot

plotter = BasicPlot()


###############################
plotter.clearPlot()

# Make the plot for the velocity
plotter.subplot(2,1,1)

t1 = np.arange(0,4.01,0.1)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,4.1,
                  -4.0,1.0,4.1)
plotter.setAxesBounds(0.0,4.1,-4.1,4.1)
plotter.axesDecorations("Moving Object's Kinematics",'','velocity  (m/sec)')

## make the empty plot for the distance
plotter.subplot(2,1,2)
plotter.addFunction(t1,5*np.exp(-3.7*t1)-2,'k-',2.0)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,4.1,
                  -5.0,2.0,5.1)
plotter.setAxesBounds(-0.1,4.1,-5.1,5.1)
plotter.axesDecorations('','Time (sec)','Position (m)')

#plt.show()
plt.savefig('velocityPlot_HW_6_week2Day3.pgf',format='pgf')
exit(0)

###############################
plotter.clearPlot()

# Make the plot for the velocity
plotter.subplot(2,1,1)

t1 = np.arange(0,4.01,0.1)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,4.1,
                  -4.0,1.0,4.1)
plotter.setAxesBounds(0.0,4.1,-4.1,4.1)
plotter.axesDecorations("Moving Object's Kinematics",'','velocity  (m/sec)')

## make the empty plot for the distance
plotter.subplot(2,1,2)
plotter.addInterpolant([[0,-3],[1,0],[2,0],[2,0],[4,4]],t1,'k-',2.0)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,4.1,
                  -5.0,2.0,5.1)
plotter.setAxesBounds(-0.1,4.1,-5.1,5.1)
plotter.axesDecorations('','Time (sec)','Position (m)')

#plt.show()
plt.savefig('velocityPlot_HW_5_week2Day3.pgf',format='pgf')
exit(0)

###############################
plotter.clearPlot()

# Make the plot for the velocity
plotter.subplot(2,1,1)

t1 = np.arange(0,4.01,0.1)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,4.1,
                  -4.0,1.0,4.1)
plotter.setAxesBounds(0.0,4.1,-4.1,4.1)
plotter.axesDecorations("Moving Object's Kinematics",'','velocity  (m/sec)')

## make the empty plot for the distance
plotter.subplot(2,1,2)
plotter.addInterpolant([[0,3],[2,-1],[4,2]],t1,'k-',2.0)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,4.1,
                  -5.0,2.0,5.1)
plotter.setAxesBounds(-0.1,4.1,-5.1,5.1)
plotter.axesDecorations('','Time (sec)','Position (m)')

#plt.show()
plt.savefig('velocityPlot_HW_4_week2Day3.pgf',format='pgf')
exit(0)


###############################
plotter.clearPlot()

# Make the plot for the velocity
plotter.subplot(2,1,1)

t1 = np.arange(0,4.01,0.1)
plotter.addInterpolant([[0,-3],[1,0],[1,0],[2,-1],[3,0],[4,2]],t1,'k-',2.0)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,4.1,
                  -4.0,1.0,4.1)
plotter.setAxesBounds(0.0,4.1,-4.1,4.1)
plotter.axesDecorations("Moving Object's Kinematics",'','velocity  (m/sec)')

## make the empty plot for the distance
plotter.subplot(2,1,2)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,4.1,
                  -5.0,2.0,5.1)
plotter.setAxesBounds(-0.1,4.1,-5.1,5.1)
plotter.axesDecorations('','Time (sec)','Position (m)')

#plt.show()
plt.savefig('velocityPlot_HW_3_week2Day3.pgf',format='pgf')
exit(0)

###############################
plotter.clearPlot()

# Make the plot for the velocity
plotter.subplot(2,1,1)

t1 = np.arange(0,4.01,0.1)
plotter.addInterpolant([[0,3],[1,0],[1,0],[2,1],[3,0],[3,0],[4,1]],t1,'k-',2.0)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,4.1,
                  -4.0,1.0,4.1)
plotter.setAxesBounds(0.0,4.1,-4.1,4.1)
plotter.axesDecorations("Moving Object's Kinematics",'','velocity  (m/sec)')

## make the empty plot for the distance
plotter.subplot(2,1,2)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,4.1,
                  -5.0,2.0,5.1)
plotter.setAxesBounds(-0.1,4.1,-5.1,5.1)
plotter.axesDecorations('','Time (sec)','Position (m)')

#plt.show()
plt.savefig('velocityPlot_HW_2_week2Day3.pgf',format='pgf')
exit(0)

###############################
plotter.clearPlot()

# Make the plot for the velocity
plotter.subplot(2,1,1)

t1 = np.arange(0,4.01,0.1)
plotter.addInterpolant([[0,-3],[2,3],[4,-2]],t1,'k-',2.0)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,4.1,
                  -4.0,1.0,4.1)
plotter.setAxesBounds(0.0,4.1,-4.1,4.1)
plotter.axesDecorations("Moving Object's Kinematics",'','velocity  (m/sec)')

## make the empty plot for the distance
plotter.subplot(2,1,2)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,4.1,
                  -5.0,2.0,5.1)
plotter.setAxesBounds(-0.1,4.1,-5.1,5.1)
plotter.axesDecorations('','Time (sec)','Position (m)')

#plt.show()
plt.savefig('velocityPlot_HW_1_week2Day3.pgf',format='pgf')
exit(0)


###############################
plotter.clearPlot()

# Make the plot for the velocity
plotter.subplot(2,1,1)

t1 = np.arange(0,4.01,0.1)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,4.1,
                  -4.0,1.0,4.1)
plotter.setAxesBounds(0.0,4.1,-4.1,4.1)
plotter.axesDecorations("Moving Object's Kinematics",'','velocity  (m/sec)')

## make the empty plot for the distance
plotter.subplot(2,1,2)
plotter.addInterpolant([[0,2],[1,-1],[3,1],[4,-1]],t1,'k-',2.0)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,4.1,
                  -3.0,2.0,3.1)
plotter.setAxesBounds(-0.1,4.1,-3.1,3.1)
plotter.axesDecorations('','Time (sec)','Position (m)')

#plt.show()
plt.savefig('velocityPlot_Class_5_week2Day3.pgf',format='pgf')
exit(0)

###############################
plotter.clearPlot()

# Make the plot for the velocity
plotter.subplot(2,1,1)

t1 = np.arange(0,4.01,0.1)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,4.1,
                  -4.0,1.0,4.1)
plotter.setAxesBounds(0.0,4.1,-4.1,4.1)
plotter.axesDecorations("Moving Object's Kinematics",'','velocity  (m/sec)')

## make the empty plot for the distance
plotter.subplot(2,1,2)
plotter.addInterpolant([[0,-2],[1,0],[2,1],[4,0]],t1,'k-',2.0)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,4.1,
                  -3.0,2.0,3.1)
plotter.setAxesBounds(-0.1,4.1,-3.1,3.1)
plotter.axesDecorations('','Time (sec)','Position (m)')

#plt.show()
plt.savefig('velocityPlot_Class_4_week2Day3.pgf',format='pgf')
exit(0)


###############################
plotter.clearPlot()

# Make the plot for the velocity
plotter.subplot(2,1,1)

t1 = np.arange(0,4.01,0.03)
plotter.addFunction(t1,2*np.exp(-2.1*(t1-1)*(t1-1))-2,'k-',2.0)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,4.1,
                  -4.0,1.0,4.1)
plotter.setAxesBounds(0.0,4.1,-4.1,4.1)
plotter.axesDecorations("Moving Object's Kinematics",'','velocity  (m/sec)')

## make the empty plot for the distance
plotter.subplot(2,1,2)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,4.1,
                  -3.0,2.0,8.1)
plotter.setAxesBounds(-0.1,4.1,-3.1,8.1)
plotter.axesDecorations('','Time (sec)','Position (m)')

#plt.show()
plt.savefig('velocityPlot_Class_3_week2Day3.pgf',format='pgf')
exit(0)

###############################
plotter.clearPlot()

# Make the plot for the velocity
plotter.subplot(2,1,1)

t1 = np.arange(0,4.01,0.1)
plotter.addInterpolant([[0,3],[1,0],[1,0],[3,2],[4,-2]],t1,'k-',2.0)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,4.1,
                  -4.0,1.0,4.1)
plotter.setAxesBounds(0.0,4.1,-4.1,4.1)
plotter.axesDecorations("Moving Object's Kinematics",'','velocity  (m/sec)')

## make the empty plot for the distance
plotter.subplot(2,1,2)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,4.1,
                  -3.0,2.0,8.1)
plotter.setAxesBounds(-0.1,4.1,-3.1,8.1)
plotter.axesDecorations('','Time (sec)','Position (m)')

#plt.show()
plt.savefig('velocityPlot_Class_2_week2Day3.pgf',format='pgf')
#exit(0)

###############################
plotter.clearPlot()

# Make the plot for the velocity
plotter.subplot(2,1,1)

t1 = np.arange(0,4.01,0.1)
plotter.addInterpolant([[0,4],[2,-3],[4,3]],t1,'k-',2.0)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,4.1,
                  -4.0,1.0,4.1)
plotter.setAxesBounds(0.0,4.1,-4.1,4.1)
plotter.axesDecorations("Moving Object's Kinematics",'','velocity  (m/sec)')

## make the empty plot for the distance
plotter.subplot(2,1,2)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,4.1,
                  -3.0,2.0,8.1)
plotter.setAxesBounds(-0.1,4.1,-3.1,8.1)
plotter.axesDecorations('','Time (sec)','Position (m)')

#plt.show()
plt.savefig('velocityPlot_Class_1_week2Day3.pgf',format='pgf')
exit(0)

###############################
plotter.clearPlot()

# Make the plot for the velocity
plotter.subplot(2,1,1)

plotter.addFunction([0,4],[4,-3],'k-',2.0)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,4.1,
                  -4.0,1.0,4.1)
plotter.setAxesBounds(0.0,4.1,-4.1,4.1)
plotter.axesDecorations('Velocity of an Object','','velocity  (m/sec)')

## make the empty plot for the distance
plotter.subplot(2,1,2)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,4.1,
                  -2.0,2.0,8.1)
plotter.setAxesBounds(-0.1,4.1,-1.1,6.1)
plotter.axesDecorations('Position of an Object','Time (sec)','Position (m)')

#plt.show()
plt.savefig('velocityPlot_week2Day3.pgf',format='pgf')


###############################
plotter.clearPlot()

def g(t):
    return(3.0/2.0*t*t*t-6.0*t*t+11.0/2.0*t)

t = np.arange(0.0,3.3,0.1)
plotter.addFunction(t,g(t)-1.0,'k-',2.0)
plotter.placeText(1.0,0.1,"A")
plotter.addFunction(t,g(t)+0.0,'k-',2.0)
plotter.placeText(1.0,1.1,"B")
plotter.addFunction(t,g(t)+1.0,'k-',2.0)
plotter.placeText(1.0,2.1,"C")
plotter.addFunction(t,g(t)+2.0,'k-',2.0)
plotter.placeText(1.0,3.1,"D")
plotter.setupGrid(0.3,'--',
                  0.0,1.0,3.1,
                  -3.0,0.5,5.1)
plotter.setAxesBounds(0.0,3.1,-3.1,5.1)
plotter.axesDecorations(r'Position Of An Object Whose Velocity Is $\frac{3}{2}t^3-6t^2+\frac{11}{2}t$','time (sec)','Position  (m/sec)')

#plt.show()
plt.savefig('whichAntiderivative_week2Day3.pgf',format='pgf')

###############################
plotter.clearPlot()

# Make the plot for the velocity
plotter.subplot(2,1,1)

plotter.addFunction([0,2],[4,0],'k-',2.0)
plotter.addFunction([2,4],[0,4],'k-',2.0)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,4.1,
                  -1.0,1.0,5.1)
plotter.setAxesBounds(0.0,4.1,-1.1,5.1)
plotter.axesDecorations('Velocity of an Object','','velocity  (m/sec)')

## make the empty plot for the distance
plotter.subplot(2,1,2)
plotter.setupGrid(0.3,'--',
                  0.0,1.0,4.1,
                  -1.0,2.0,6.1)
plotter.setAxesBounds(-0.1,4.1,-1.1,6.1)
plotter.axesDecorations('Position of an Object','Time (sec)','Position (m)')


#plt.show()
plt.savefig('noContDeriv_week2Day3.pgf',format='pgf')
