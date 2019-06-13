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


get_largest_factor <- function(n) {
    biggest_prime = 2
    primes = get_primes(ceiling(sqrt(n)))
        for (prime in primes) {
            while (n %% prime == 0) {
                n = n / prime
                biggestprime = prime
            }
        }
    if (n == 1) return(biggestprime)
    return(n)
}