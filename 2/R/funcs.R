fibonacci <- function(limit) {
    i = 0
    j = 1
    result = c()
    while(i <= limit) {
        result = append(result, i)
        i = j
        j = j + result[length(result)]
    }
    return(result)
}

sum_even_fibonacci <- function(limit) {
    fibo = fibonacci(limit)
    sum_fibo = 0
    for (num in fibo) {
        if (num %% 2 == 0) {
            sum_fibo = sum_fibo + num
        }
    }
    return(sum_fibo)
}
