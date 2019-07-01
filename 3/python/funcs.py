def primes(limit):
    '''
    Find all primes up to the limit. Returns generator which iterates through
    each prime once.
    '''
    primes = [True] * (limit + 1)
    i = 2
    while i <= limit:
        if primes[i]:
            yield(i)
            for k in range(i, limit + 1, i):
                primes[k] = False
        i += 1

def find_factors(n):
    for prime in primes(int(n ** 0.5)):
        while (n % prime == 0):
            n /= prime
        if n == 1:
            return prime
    return n