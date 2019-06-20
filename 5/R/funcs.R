get_primes <- function(limit) {
    sieve = rep(TRUE, limit)
    primes = c()

    sieve[1] = FALSE

    for (k in 1:length(sieve)) {
        if(sieve[k]) {
            primes = append(primes, k)
            sieve[seq(from = k, by = k, to = limit)] = FALSE
        }
    }
    return(as.numeric(primes))
}


get_factors <- function(n) {
    factors = c()
    primes = get_primes(n)
        for (prime in primes) {
            while (n %% prime == 0) {
                n = n / prime
                factors = c(factors, prime)
            }
        }
    return(factors)
}

find_divisors <- function(n) {
    foo = c()
    for (test in lapply(as.list(n), get_factors)) {
        for (val in unique(test)) {
            if(is.null(foo[toString(val)])) {
                foo[toString(val)] = sum(test == val)
            }


            if (is.na(foo[toString(val)])) {
                foo[toString(val)] = sum(test == val)
            }
            if (foo[toString(val)] < sum(test == val)) {
                foo[toString(val)] = sum(test == val)
            }
        }
    }
    return(foo)
}