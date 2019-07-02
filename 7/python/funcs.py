import math


def primes(n):
    '''
    Use p(n) ~ n (log n + log log n - 1) as approximation for value of n-th prime
    '''
    limit = math.ceil(n * (math.log(n) + math.log(math.log(n)) - 1) * 1.01)
    primes = [True] * (limit + 1)
    i = 2
    while i <= limit:
        if primes[i]:
            yield(i)
            for k in range(i, limit + 1, i):
                primes[k] = False
        i += 1

print([x for x in primes(10001)][10000])