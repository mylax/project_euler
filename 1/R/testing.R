library(unittest, quietly = TRUE)
source("funcs.R")
ok(identical(find_multiples(c(3, 5), 10), c(3, 5, 6, 9)),
     "multiples 3 or 5 up to but not including ten")


ok(identical(find_multiples(c(3, 5), 10), c(3, 5, 6, 9, 10)),
     "multiples 3 or 5 up to but not including ten")