x = c(0:20)/50
y = rnorm(21,sd=0.2)-x/10

x1 = c(x,4);
y1 = c(y,3.8)
a = format(cor(x1,y1),digits=2)
title = paste("Correlation = ",a)
png(filename="correlation1.png",width=420,height=420)
plot(x1,y1,xlim=c(-2,5),ylim=c(-2,5),main=title)
dev.off()
postscript(file="correlation1.eps",width=4,height=4,
           horizontal = FALSE, onefile = FALSE, paper = "special",
           family = "ComputerModern", encoding = "TeXtext.enc")
plot(x1,y1,xlim=c(-2,5),ylim=c(-2,5),main=title)
dev.off()

png(filename="correlation2.png",width=420,height=420)
plot(x1,y1,xlim=c(-2,5),ylim=c(-2,5),main=title)
fit1 = lm(y1 ~ x1)
abline(fit1)
dev.off()
postscript(file="correlation2.eps",width=4,height=4,
           horizontal = FALSE, onefile = FALSE, paper = "special",
           family = "ComputerModern", encoding = "TeXtext.enc")
plot(x1,y1,xlim=c(-2,5),ylim=c(-2,5),main=title)
abline(fit1)
dev.off()


png(filename="correlation3.png",width=420,height=420)
a = format(cor(x,y),digits=2)
title = paste("Correlation = ",a)
plot(x,y,xlim=c(-2,5),ylim=c(-2,5),main=title)
dev.off()
postscript(file="correlation3.eps",width=4,height=4,
           horizontal = FALSE, onefile = FALSE, paper = "special",
           family = "ComputerModern", encoding = "TeXtext.enc")
plot(x,y,xlim=c(-2,5),ylim=c(-2,5),main=title)
dev.off()

png(filename="correlation4.png",width=420,height=420)
fit = lm(y ~ x)
plot(x,y,xlim=c(-2,5),ylim=c(-2,5),main=title)
abline(fit)
dev.off()
postscript(file="correlation4.eps",width=4,height=4,
           horizontal = FALSE, onefile = FALSE, paper = "special",
           family = "ComputerModern", encoding = "TeXtext.enc")
plot(x,y,xlim=c(-2,5),ylim=c(-2,5),main=title)
abline(fit)
dev.off()
