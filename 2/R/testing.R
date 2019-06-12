library(unittest, quietly = TRUE)
source("funcs.R")

ok(identical(fibonacci(0), c(0)),
     "fibonacci numbers up to zero")

ok(identical(fibonacci(10), c(0, 1, 1, 2, 3, 5, 8)),
     "fibonacci numbers up to ten")


ok(identical(sum_even_fibonacci(10),10),
     "sum even fibonacci numbers up to 10")


ok(identical(sum_even_fibonacci(20),10),
     "sum even fibonacci numbers up to 20")


ok(identical(sum_even_fibonacci(0),0),
     "sum even fibonacci numbers up to 0")