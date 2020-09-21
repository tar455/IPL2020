
install.packages("rvest")
library(rvest)

url <- "https://www.iplt20.com/match/2020/01?tab=scorecard"
website <- read_html(url)
datain_web <-html_table(website,header<-NA,trim<- TRUE,fill <-FALSE,dec=".")
print(datain_web)
print("This project perform  Analysis on IPL 2020")
print("Let's ready for that")
