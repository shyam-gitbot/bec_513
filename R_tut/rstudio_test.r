new_air = airquality

list_of_mean = apply(new_air,2,mean,na.rm=TRUE)
list_of_mean

all_na = (which(is.na(airquality), arr.ind = T))
all_na[,2]
list_of_mean[all_na[,2]]

new_air[all_na] <- list_of_mean[all_na[,2]]
new_air

st = "cC"
st_l =strsplit(st,split = "")[[1]]
mean(st_l %in% c("C","c"))

str(st_l)

thisfxn <- function(a=1,b=2,c=3){
  ans = mean(c(a,b,c))
  ans
}



print(thisfxn())
mean(c(1,2,3))

