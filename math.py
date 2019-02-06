# -*- coding: utf-8 -*-

import functools


def prime_generator(n):
    """Return all primes smaller n as list."""
    
    primes = [True for x in list(range(n))]
    
    p = 2
    while p * p < n:
        if p:
            for i in range(p*2, n, p):
                primes[i] = False
        p += 1
        
    return [i for i, prime in enumerate(primes) if prime and i != 0]


primes = prime_generator(50045010)
 


def factor_generator(n, *primes):
    """Return all prime factors of n and how often they occur. 
    E.g. 4 returns (2,2), 100 returns (2,2) (5, 2).
    
    Keyword arguments:
    n -- int -- find all the prime factors and how often they occur for this number
    primes -- list of int -- optional, list of primes to speed up calculation
    if primes is not provided calculate primes in the function call 
    """
    if primes is None: # check if primes have been provided or have to be cacluated
        primes = prime_generator(n)
        
    primes_factors = [prime for prime in primes if n % prime == 0]
    while True:
        trianglenew = n
        for prime in primes_factors:
            trianglenew = trianglenew / prime
        primes_factors.extend([prime for prime in primes if trianglenew % prime == 0])
        if trianglenew == 1:
            break
        
    return [(prime, primes_relevant.count(prime)) for prime in set(primes_relevant) if prime != 1]
        

def divisor_generator(n, *primes):
    """Return all divisors of n as list.
    
    Keyword arguments:
    n -- int -- find all the divisors for this number
    primes -- list of int -- optional, list of primes to speed up calculation
    if primes is not provided calculate primes in the function call 
    """
    factors = factor_generator(n, primes)
    nfactors = len(factors)
    f = [0] * nfactors
    divisors = []    
    while True:
        divisors.append(functools.reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1))
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return divisors
       
i = 3375
while True:
    n = sum(range(i))
    divisors_count = len(divisor_generator(n, primes))
    print([i, divisors_count, n])
    if divisors_count > 499:
        break
    i += 1


    
    
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

