tuits<-read.xlsx("./TweetsNEgativoVenezolanos2018.xlsx",sheet = 1)
names(tuits)
summary(tuits$Followers)

tuitsVenezolano<-filter(tuits, grepl('venezolanos|venecos|venecas|Venezolano|venezolana|venezolanas',Contents))
write.xlsx(tuitsVenezolano,"./datos_propios/tuitsVenezolano.xlsx")
hist(tuitsVenezolano$Followers)

tuitsVenezolano$Followers_cat<-as.factor(cut(tuitsVenezolano$Followers,breaks=c(-Inf, 192,563,1501,Inf)))
levels(tuitsVenezolano$Followers_cat)<-c("1er Cuartil (<191)", "2er Cuartil (193:563)","3er Cuartil (564:1501)","4to Cuartil (>1501)")  
barchart(tuitsVenezolano$Followers_cat)
write.xlsx(tuitsVenezolano,"./datos_propios/tuitsVenezolano.xlsx")
tabla<-as.data.frame(table(tuitsVenezolano$`Province/State`,tuitsVenezolano$Sentiment))
write.csv(tabla, './sent_dep.csv')
