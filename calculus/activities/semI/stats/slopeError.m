

x = 0:0.1:8;
y = exp(x/4);

xbar = 5;
delta=2.5;

ybar = exp(xbar/4);
slope=ybar/4;
change = delta*slope;

clf

%XTick = [ (1 by 11) double array]
%XTickLabel = [ (11 by 3) char array]
%XTickLabelMode = auto
%XTickMode = auto

hold on
plot(x,y,'k-','LineWidth',3)
axis([min(x) max(x) 0 max(y)])
set(gca,'XTickLabelMode','manual')
set(gca,'XTick',[(xbar-delta) xbar (xbar+delta)])
set(gca,'XTickLabel',{'x-dx';'x';'x+dx'})


set(gca,'YTickLabelMode','manual')
set(gca,'YTick',[(ybar-change) ybar (ybar+change)])
set(gca,'YTickLabel',{'f-error';'f';'f+error'})

xSlope = (xbar-delta):0.05:(xbar+delta);
ySlope = slope*(xSlope-xbar)+ybar;
plot(xSlope,ySlope,'k--','LineWidth',2.2)

plot([0 xbar-delta xbar-delta],[min(ySlope) min(ySlope) 0],'k:','LineWidth',1.5)
plot([0 xbar+delta xbar+delta],[max(ySlope) max(ySlope) 0],'k:','LineWidth',1.5)
plot([0 xbar xbar],[ybar ybar 0],'k:','LineWidth',1.5)

%xlabel('x')
%ylabel('f')
title('Approximation of the Error Using the Slope')


print -deps slopeError.eps
print -dpng slopeError.png

