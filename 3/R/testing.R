library(unittest, quietly = TRUE)
source("funcs.R")

ok(identical(get_primes(10), c(2, 3, 5, 7)),
     "get primes up to ten")

ok(identical(get_primes(7), c(2, 3, 5, 7)),
     "get primes up to 7")

ok(identical(get_primes(6), c(2, 3, 5)),
     "get primes up to 6")


ok(identical(get_largest_factor(7), 7),
     "get largest prime factor of 7")


ok(identical(get_largest_factor(30), 5),
     "get largest prime factor of 30")