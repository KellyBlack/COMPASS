c <- read.csv(file='cavendish.csv',head=TRUE,sep=',')
mc <- mean(c$density)
sdc <- sd(c$density)

cat('The mean is ',mc,'\n')
cat('the sample standard deviation is ',sdc,'\n')

ci <- qnorm(.95)*sdc/sqrt(length(c$density))
cat('The width of the confidence interval is 2*',ci,'\n');
cat('The confidence level is from ',
     mc-ci,' to ',mc+ci,'\n')



