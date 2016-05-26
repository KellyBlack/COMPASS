x <- c(0,1.5,2,2.5,12)
y <- 2*x + 4 + rnorm(5,sd=1)
plot(x,y)
fit <- lm(y ~ x)
abline(fit)
curve(predict(fit,data.frame(x=x),interval="confidence")[,2],add=T,col="red",type="l",lty=c(4,4))
curve(predict(fit,data.frame(x=x),interval="confidence")[,3],add=T,type="l",col="red",lty=c(4,4))

