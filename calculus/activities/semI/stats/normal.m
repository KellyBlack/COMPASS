

x = -10:0.05:20;
x0Bad = 7;
sigma = 3.5;
y = exp(-((x-x0Bad)/sigma).^2)/sqrt(pi*sigma);

clf

%XTick = [ (1 by 11) double array]
%XTickLabel = [ (11 by 3) char array]
%XTickLabelMode = auto
%XTickMode = auto

hold on
axis([-10 20 0 0.35])
set(gca,'XTickLabelMode','manual')
set(gca,'XTick',[(x0Bad-2*sigma):sigma:(x0Bad+2*sigma)])
set(gca,'XTickLabel',{' ';' ';' ';' ';' '})
%set(gca,'XTickLabel',{'\mu-2\sigma';'\mu-\sigma';'\mu';'\mu+\sigma';'\mu+2\sigma'})
text(x0Bad-2*sigma,-0.01,'\mu-2\sigma')
text(x0Bad-sigma,-0.01,'\mu-\sigma')
text(x0Bad,-0.01,'\mu')
text(x0Bad+sigma,-0.01,'\mu+\sigma')
text(x0Bad+2*sigma,-0.01,'\mu+2\sigma')

set(gca,'YTick',0:1:1)
%set(gca,'YTickLabelMode','manual')


plot(x,y,'k-');

%xbar = -10:0.05:5;
%ybar = exp(-((xbar-x0Bad)/sigma).^2)/sqrt(pi*sigma);
%a = area(xbar,ybar,'FaceColor',[0.85 0.85 0.85],'LineStyle','--');
%set(a,'FaceColor',[1.0 0.85 0.85]);
%set(a,'FaceColor',[0.85 0.85 0.85]);


xlabel('x')
ylabel('p')
title('Normal Distribution with Mean \mu')


print -deps normal.eps
print -dpng normal.png

