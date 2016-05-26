
# Problem 3.1 / stem/leaf plots
prob31 <- c(17,18,9,41,46,16,34,39,9,9,14,12,19,8)
prob31
sort(prob31)
stem(prob31)

png(filename = "prob33.png", width = 480, height = 480)
hist(prob31,main='Histogram for Problem 3.3',xlab='Numbers')
dev.off()

postscript(file = "prob33.eps", width = 4, height = 4,
            horizontal = FALSE, onefile = FALSE, paper = "special",
           family = "ComputerModern", encoding = "TeXtext.enc")
hist(prob31,main='Histogram for Problem 3.3',xlab='Numbers')
dev.off()

summary(prob31)

png(filename = "prob35.png", width = 480, height = 480)
boxplot(prob31)
dev.off()

postscript(file = "prob35.eps", width = 4, height = 4,
            horizontal = FALSE, onefile = FALSE, paper = "special",
           family = "ComputerModern", encoding = "TeXtext.enc")
boxplot(prob31)
dev.off()



# Problem 3.2 stem/leaf plots
prob32 <- c(1.5,7.0,0.6,4.5,3.7,5.7,8.0,1.6,3.8,2.7,2.0,7.1)
prob32
sort(prob32)
stem(prob32)

png(filename = "prob34.png", width = 480, height = 480)
hist(prob32,main='Histogram for Problem 3.4',xlab='Numbers')
dev.off()

postscript(file = "prob34.eps", width = 4, height = 4,
            horizontal = FALSE, onefile = FALSE, paper = "special",
           family = "ComputerModern", encoding = "TeXtext.enc")
hist(prob32,main='Histogram for Problem 3.4',xlab='Numbers')
dev.off()

png(filename = "prob36.png", width = 480, height = 480)
boxplot(prob32)
dev.off()

postscript(file = "prob36.eps", width = 4, height = 4,
            horizontal = FALSE, onefile = FALSE, paper = "special",
           family = "ComputerModern", encoding = "TeXtext.enc")
boxplot(prob32)
dev.off()



x <- seq(0,5,1)
y <- c(1.00,1.09,1.17,1.23,1.28,1.31)
