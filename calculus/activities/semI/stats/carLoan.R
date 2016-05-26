year <- c(2000 ,   2001  ,  2002  ,  2003 ,   2004)
rate <- c(9.34 ,   8.50  ,  7.62  ,  6.93  ,  6.60)
png(filename = "bankRates.png", width = 480, height = 480)
plot(year,rate,
     main="Commercial Banks Interest Rate for 4 Year Car Loan",
     sub="http://www.federalreserve.gov/releases/g19/20050805/")
dev.off()
postscript(file="bankRates.eps",width=4,height=4,
           horizontal = FALSE, onefile = FALSE, paper = "special",
           family = "ComputerModern", encoding = "TeXtext.enc")
plot(year,rate,
     main="Commercial Banks Interest Rate for 4 Year Car Loan",
     sub="http://www.federalreserve.gov/releases/g19/20050805/")
dev.off()

cor(year,rate)
fit <- lm(rate ~ year)

png(filename = "bankRatesFit.png", width = 480, height = 480)
plot(year,rate,
     main="Commercial Banks Interest Rate for 4 Year Car Loan",
     sub="http://www.federalreserve.gov/releases/g19/20050805/")
abline(fit)
dev.off()
postscript(file="bankRatesFit.eps",width=4,height=4,
           horizontal = FALSE, onefile = FALSE, paper = "special",
           family = "ComputerModern", encoding = "TeXtext.enc")
plot(year,rate,
     main="Commercial Banks Interest Rate for 4 Year Car Loan",
     sub="http://www.federalreserve.gov/releases/g19/20050805/")
abline(fit)
dev.off()


fit
fit$coefficients[1]
fit$coefficients[2]
fit$coefficients[[1]]
fit$coefficients[[2]]
summary(fit)


yearSmear = c()
rateSmear = c()
n = 50;
for(i in 1:length(year)){
  yearSmear = c(yearSmear,rep(year[i],n))
  rateSmear = c(rateSmear,rate[i]+rnorm(n,sd=0.6))
}

print(cor(yearSmear,rateSmear))
print(cor(year,rate))
fitSmear <- lm(rateSmear ~ yearSmear)
print(summary(fit))
print(summary(fitSmear))

png(filename = "bankRatesSmear.png", width = 480, height = 480)
plot(yearSmear,rateSmear,
     main="Commercial Banks Interest Rate for 4 Year Car Loan",
     sub="http://www.federalreserve.gov/releases/g19/20050805/")
a = format(cor(yearSmear,rateSmear),digits=2)
text(2001,5.5,paste("Correlation = ",a))
abline(fit)
dev.off()
postscript(file="bankRatesSmear.eps",width=4,height=4,
           horizontal = FALSE, onefile = FALSE, paper = "special",
           family = "ComputerModern", encoding = "TeXtext.enc")
plot(yearSmear,rateSmear,
     main="Commercial Banks Interest Rate for 4 Year Car Loan",
     sub="http://www.federalreserve.gov/releases/g19/20050805/")
a = format(cor(yearSmear,rateSmear),digits=2)
text(2001,5.5,paste("Correlation = ",a))
abline(fit)
dev.off()

