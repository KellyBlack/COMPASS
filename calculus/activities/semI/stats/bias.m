
%offCenter   = random('normal',0.70,0.1 ,1,12);
%onCenter    = random('normal',0.50,0.1 ,1,12);
%wideSpread  = random('normal',0.50,0.05,1,12);
%closeSpread = random('normal',0.50,0.2 ,1,12);

%data = [offCenter;onCenter;wideSpread;closeSpread];

clf;
set(1,'Color',[1.0 1.0 1.0]);
set(1,'PaperPositionMode','auto');
set(1,'PaperPosition',[0.541176 4.31765 7.4 2.37647]);
label=['A','B','C','D'];
for col=1:2,
  for row=1:2,

    subplot(2,2,2*(col-1)+row)
    ax = get(1,'CurrentAxes');
    
    hold on;
    plot(data(2*(col-1)+row,:),0*data(2*(col-1)+row,:),'ko');
    set(ax,'visible','off')
    axis([0 1 -.3 .3]);
    plot([0 1],[0 0],'k-');
    plot([.5 .5],[-.05 .05],'k-')
    text(.5,-.1,'X')
    text(.2,.2,label(2*(col-1)+row))
    
  end
end

print -dpng bias.png
print -deps bias.eps


