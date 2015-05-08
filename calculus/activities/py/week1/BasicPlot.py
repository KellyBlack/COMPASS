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

    def setAxesBounds(self,lowx,highx,lowy,highy):
        plt.xlim([lowx,highx])
        plt.ylim([lowy,highy])

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
        ax.set_xticks(np.arange(startx,endx,deltax))
        ax.set_yticks(np.arange(starty,endy,deltay))

        ax.xaxis.grid(linewidth=thickness)
        ax.yaxis.grid(linewidth=thickness)
        plt.grid(True)

    def xAxisTicks(self,positions,labels,rot="horizontal",margins=0.2):
        plt.xticks(positions,labels,rotation=rot)
        plt.margins(margins)

    def yAxisTicks(self,positions,labels,rot="horizontal",margins=0.2):
        plt.yticks(positions,labels,rotation=rot)
        plt.margins(margins)


    def axesDecorations(self,title,horiztonalLabel,verticallabel):

        plt.xlabel(horiztonalLabel)
        plt.ylabel(verticallabel)
        plt.title(title)

    def placeText(self,xpos,ypos,text,**kwargs):
        plt.text(xpos,ypos,text,kwargs)

    def clearPlot(self):
        plt.clf()

    def markJumps(self,jumps,symbolSize):
        for jump in jumps:
            if(jump[2]):
                plt.plot(jump[0],jump[1],'ok',markersize=symbolSize,mfc='black')
            else:
                plt.plot(jump[0],jump[1],'ok',markersize=symbolSize,mfc='white')

    def subplot(self,row,col,number):
        plt.subplot(row,col,number)


if (__name__ =='__main__') :
    plotter = BasicPlot()

    #plt.xkcd(randomness=0.1)
    #with plt.xkcd():
    plotter.clearPlot()

    with plt.xkcd():
        plotter.addFunction([0,1,2,3],[0,-1.0,2,1], 'k-',2.0)
        plotter.setupGrid(0.5,'--',
                          0.0,1.0,3.0,
                         -1.0,0.5,2.0,)
        plotter.axesDecorations('Position of an Object','Time (sec)','Position (m)')
        #plt.text(1.0,3.025, r'$\alpha=100,\ \sigma=15$'


    plotter.setAxesBounds(0.0,3.05,-1.05,2.05)
    plt.show()
    #plt.savefig('preClass3.pgf')

