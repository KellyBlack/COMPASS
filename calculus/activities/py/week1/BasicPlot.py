#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt


class BasicPlot:

    def __init__(self):
        self.clearPlot()


    def clearPlot(self):
        plt.clf()

    def addFunction(self,domain,range,format,width=2.0):
        plt.plot(domain,range,format,linewidth=width)

    def setupGrid(self,thickness=1.0,style='--',
                  startx=0.0,deltax=0.1,endx=1.0,
                  starty=0.0,deltay=0.1,endy=1.0):

        ax = plt.gca()
        xticklines = plt.getp(ax, 'xticklines')
        yticklines = plt.getp(ax, 'yticklines')
        xgridlines = plt.getp(ax, 'xgridlines')
        ygridlines = plt.getp(ax, 'ygridlines')
        xticklabels = plt.getp(ax, 'xticklabels')
        yticklabels = plt.getp(ax, 'yticklabels')

        plt.setp(xticklines, 'linewidth', thickness)
        plt.setp(yticklines, 'linewidth', thickness)
        plt.setp(xgridlines, 'linestyle', style)
        plt.setp(ygridlines, 'linestyle', style)
        plt.setp(yticklabels, 'color', 'k', fontsize='medium')
        plt.setp(xticklabels, 'color', 'k', fontsize='medium')
        ax.set_yticks(np.arange(startx,endx,deltax))
        ax.set_xticks(np.arange(starty,endy,deltay))

        plt.grid(True)

    def axesDecorations(self,title,horiztonalLabel,verticallabel):

        plt.xlabel(horiztonalLabel)
        plt.ylabel(verticallabel)
        plt.title(title)



if (__name__ =='__main__') :
    pass
