find_multiples <- function(k,  n) {
    multiples = c()
    for (i in k) {
        multiples <- c(multiples, seq(i, n-1, i))
    }
    return(sort(unique(multiples)))
}