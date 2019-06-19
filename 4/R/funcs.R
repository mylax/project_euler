revert_num <- function(x) {
    return(as.numeric(paste(rev(strsplit(toString(x), "")[[1]]), collapse ="")))
}


find_palindromic <- function(n1, n2) {
    result = 0
    for (i in seq(n1)) {
        for (j in seq(n2)) {
            prod = i * j
            if (revert_num(prod) == prod & prod > result) {
                result = prod
                largest_n1 = i
                largest_n2 = j
            }
        }
    }
    return(c(result, largest_n1, largest_n2))
}



