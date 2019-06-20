def primes(limit):
    primes = [True] * (limit + 1)
    i = 2
    while i <= limit:
        if primes[i]:
            yield(i)
            for k in range(i, limit + 1, i):
                primes[k] = False
        i += 1

def find_all_factors(n):
    factors = []
    for prime in primes(n):
        while (n % prime == 0):
            n /= prime
            factors.append(prime)
    return factors

def find_prime_factors(n):
    if not isinstance(n, list):
        n = [n]
    divisors = {}
    for x in n:
        factors = find_all_factors(x)
        for factor in set(factors):
            try:
                if divisors[factor] < factors.count(factor):
                    divisors[factor] = factors.count(factor)
            except KeyError:
                divisors[factor] = factors.count(factor)
    return divisors