#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

#plt.xkcd(randomness=0.1)
#with plt.xkcd():

# Make the first plot
plt.plot([0,1,2,3],[0,1,1,2], 'k-',linewidth=2.0)
ax = plt.gca()
xticklines = plt.getp(ax, 'xticklines')
yticklines = plt.getp(ax, 'yticklines')
xgridlines = plt.getp(ax, 'xgridlines')
ygridlines = plt.getp(ax, 'ygridlines')
xticklabels = plt.getp(ax, 'xticklabels')
yticklabels = plt.getp(ax, 'yticklabels')

plt.setp(xticklines, 'linewidth', 3)
plt.setp(yticklines, 'linewidth', 3)
plt.setp(xgridlines, 'linestyle', '-')
plt.setp(ygridlines, 'linestyle', '-')
plt.setp(yticklabels, 'color', 'k', fontsize='medium')
plt.setp(xticklabels, 'color', 'k', fontsize='medium')
ax.set_yticks(np.arange(0.0,2.5,0.2))
ax.set_xticks(np.arange(0,3.0,0.5))

plt.grid(True)
plt.axis([0.0, 3.0, 0.0, 2.0])
plt.xlabel('Time (sec)')
plt.ylabel('Position (m)')
plt.title('Position of an Object')
#plt.text(1.0,3.025, r'$\alpha=100,\ \sigma=15$')
plt.show()


# Make the second plot
plt.plot([0,1,2,3],[0,0.5,3,2], 'k-',linewidth=2.0)
ax = plt.gca()
xticklines = plt.getp(ax, 'xticklines')
yticklines = plt.getp(ax, 'yticklines')
xgridlines = plt.getp(ax, 'xgridlines')
ygridlines = plt.getp(ax, 'ygridlines')
xticklabels = plt.getp(ax, 'xticklabels')
yticklabels = plt.getp(ax, 'yticklabels')

plt.setp(xticklines, 'linewidth', 3)
plt.setp(yticklines, 'linewidth', 3)
plt.setp(xgridlines, 'linestyle', '-')
plt.setp(ygridlines, 'linestyle', '-')
plt.setp(yticklabels, 'color', 'k', fontsize='medium')
plt.setp(xticklabels, 'color', 'k', fontsize='medium')
ax.set_yticks(np.arange(0.0,3.0,0.2))
ax.set_xticks(np.arange(0,3.0,0.5))

plt.grid(True)
plt.axis([0.0, 3.0, 0.0, 3.0])
plt.xlabel('Time (sec)')
plt.ylabel('Position (m)')
plt.title('Position of an Object')
#plt.text(1.0,3.025, r'$\alpha=100,\ \sigma=15$')
plt.show()


# Make the third plot
plt.plot([0,1,2,3],[0,-1.0,2,1], 'k-',linewidth=2.0)
ax = plt.gca()
xticklines = plt.getp(ax, 'xticklines')
yticklines = plt.getp(ax, 'yticklines')
xgridlines = plt.getp(ax, 'xgridlines')
ygridlines = plt.getp(ax, 'ygridlines')
xticklabels = plt.getp(ax, 'xticklabels')
yticklabels = plt.getp(ax, 'yticklabels')

plt.setp(xticklines, 'linewidth', 3)
plt.setp(yticklines, 'linewidth', 3)
plt.setp(xgridlines, 'linestyle', '-')
plt.setp(ygridlines, 'linestyle', '-')
plt.setp(yticklabels, 'color', 'k', fontsize='medium')
plt.setp(xticklabels, 'color', 'k', fontsize='medium')
ax.set_yticks(np.arange(-1.0,2.0,0.2))
ax.set_xticks(np.arange(0,3.0,0.5))

plt.grid(True)
plt.axis([0.0, 3.0, -1.0, 2.0])
plt.xlabel('Time (sec)')
plt.ylabel('Position (m)')
plt.title('Position of an Object')
#plt.text(1.0,3.025, r'$\alpha=100,\ \sigma=15$')
plt.show()
