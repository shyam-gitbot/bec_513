input_con <- file("stdin")
#while (length(line <- readLines(input_con, n = 1)) > 0) {
#  cat(line, "\n", sep = "") 
#}

while (input_con){
  print(line)
}


if (!requireNamespace("BiocManager", quietly = TRUE))
  install.packages("BiocManager")

BiocManager::install(c("biomaRt", "Gviz", "rtracklayer"))
