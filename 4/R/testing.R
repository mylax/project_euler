library(unittest, quietly = TRUE)
source("funcs.R")

ok(identical(revert_num(1241), 1421),
     "revert number 1241")

ok(identical(revert_num(121), 121),
     "revert number 121")

ok(identical(revert_num(0), 0),
     "revert number 0")


ok(identical(find_palindromic(10, 1)[1], as.integer(9)),
     "find palindromic up to 10 equals 9")


ok(identical(find_palindromic(100, 1)[1], as.integer(99)),
     "find palinmdromic 100 and 1 should be 99")


ok(identical(find_palindromic(10, 11)[1], as.integer(99)),
     "find palindromic 10 and 11 should be 99")