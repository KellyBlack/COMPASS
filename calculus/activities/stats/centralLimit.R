#library(sm)
N <- 200
trials <- 7;
cat('Will print out ',trials,' trials\n');
v <- c(1:N)
dev <- c(1:trials);
means <- c(1:trials);

#par(ask = FALSE)
for (i in 1:trials) {
 for (j in 1:N) {
    #v[j] <- mean(rpois(i,3))
    #v[j] <- mean(rbinom(i,5,.3))
    #v[j] <- mean(rgamma(i,6,3))
    v[j] <- mean(runif(i,0,1));
 }

 dev[i] <- sd(v);
 means[i] <- mean(v);

 #title(main = list("Stopping Distance versus Speed", cex=1.5,
 #                      col="red", font=3))

 title <- 'Sampling Evenly Distributed Random Variables'
 subTitle <- paste('Mean of ',format(i,digits=1),' Samples')
 fileName <- paste('centralLimit',format(i,digits=1,width=1),'.png',sep='')

 png(file=fileName,width=780,height=780)
 hist(v,xlim=c(0,1),ylim=c(0,65),main=title,sub=list(subTitle,cex=1.5))
 dev.off()

 fileName <- paste('centralLimit',format(i,digits=1,width=1),'.eps',sep='')
 postscript(file=fileName,width=6,height=6,
           horizontal = FALSE, onefile = FALSE, paper = "special",
           family = "ComputerModern", encoding = "TeXtext.enc")
 hist(v,xlim=c(0,1),ylim=c(0,65),main=title,sub=list(subTitle,cex=1.5))
 dev.off()

 cat (i,' Samples\n')
 #pause()
}

#par(ask = TRUE)
print('Means\n')
png(file='centralLimitMeans.png',width=660,height=660)
plot(1:trials,means,
     main='Means of the Trials',
     ylim=c(.25,.75),
     xlab='Trial',ylab='Mean')
dev.off()

postscript(file='centralLimitMeans.eps',width=5,height=5,
           horizontal = FALSE, onefile = FALSE, paper = "special",
           family = "ComputerModern", encoding = "TeXtext.enc")
plot(1:trials,means,
     main='Means of the Trials',
     ylim=c(.25,.75),
     xlab='Trial',ylab='Mean')
dev.off()


print('Standard Deviations\n');
png(file='centralLimitSTD.png',width=660,height=660)
plot(1:trials,dev,
     main='Standard Deviations of the Trials',
     xlab='Trial',ylab='Standard Deviation');
dev.off()

postscript(file='centralLimitSTD.eps',width=5,height=5,
           horizontal = FALSE, onefile = FALSE, paper = "special",
           family = "ComputerModern", encoding = "TeXtext.enc")
plot(1:trials,dev,
     main='Standard Deviations of the Trials',
     xlab='Trial',ylab='Standard Deviation');
dev.off()

