
install.packages("rvest")
library(rvest)

url <- "https://www.iplt20.com/stats/2020/most-runs"
website <- read_html(url)
datain_web <-html_table(website,header<-NA,trim<- TRUE,fill <-FALSE,dec=".")
print(datain_web[3])
print("This project perform  Analysis on IPL 2020")
print("Let's ready for that")

