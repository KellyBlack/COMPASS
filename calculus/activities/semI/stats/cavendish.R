c <- read.csv(file='cavendish.csv',head=TRUE,sep=',')
print(summary(c))
print(stem(c$density))


png(file="cavHist.png",width=640,height=480)
hist(c$density,breaks=seq(4.8,5.9,.1),xlab='Ratio of Density of the Earth to the Density of Water',ylab='Frequency',main='Cavendish\'s Measurements of the Density of the Earth',xlim=c(4.8,6.0))
dev.off()

postscript(file="cavHist.eps",width=640,height=480,horizontal=FALSE)
hist(c$density,breaks=seq(4.8,5.9,.1),xlab='Ratio of Density of the Earth to the Density of Water',ylab='Frequency',main='Cavendish\'s Measurements of the Density of the Earth',xlim=c(4.8,6.0))
dev.off()


postscript(file="cavBoxPlot.eps",horizontal=FALSE,width=240,height=540)
boxplot(c$density,main='Density of the Earth',sub='Cavendish\'s Measurements',ylab='Ratio of Density of the Earth to the Density of Water')
dev.off()

png(file="cavBoxPlot.png",width=340,height=540)
boxplot(c$density,main='Density of the Earth',sub='Cavendish\'s Measurements',ylab='Ratio of Density of the Earth to the Density of Water')
dev.off()
