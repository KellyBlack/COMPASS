x = c(-50:50)/15

png(filename="correlation.png",width=840,height=420)
par(mfcol=c(2,2))

y1 = 2*x + rnorm(101)
plot(x,y1,xlim=c(-10,10),ylim=c(-10,10),ylab="y")
title('Correlation = 0.9')

y2 = x + rnorm(101,sd=2.65)
plot(x,y2,xlim=c(-10,10),ylim=c(-10,10),ylab="y")
title('Correlation = 0.5')

y3 = rnorm(101,sd=10)
plot(x,y3,xlim=c(-10,10),ylim=c(-10,10),ylab="y")
title('Correlation = 0.0')

plot(x,-y1,xlim=c(-10,10),ylim=c(-10,10),ylab="y")
title('Correlation = -0.9')

dev.off()


postscript(file="correlation.eps",width=12,height=6,
           horizontal = FALSE, onefile = FALSE, paper = "special",
           family = "ComputerModern", encoding = "TeXtext.enc")
par(mfcol=c(2,2))
plot(x,y1,xlim=c(-10,10),ylim=c(-10,10),ylab="y")
title('Correlation = 0.9')
plot(x,y2,xlim=c(-10,10),ylim=c(-10,10),ylab="y")
title('Correlation = 0.5')
plot(x,y3,xlim=c(-10,10),ylim=c(-10,10),ylab="y")
title('Correlation = 0.0')
plot(x,-y1,xlim=c(-10,10),ylim=c(-10,10),ylab="y")
title('Correlation = -0.9')
dev.off()
