# -*- coding: utf-8 -*-



def get_primes(n):
    """Return all primes smaller n as list."""
    primes = [True] * n
    primes[0] = primes[1] = False
    for i, prime in enumerate(primes):
        if prime:
            for n in range(2 * i, (sqrt(n), i):
                primes[i] = False

    return [i for i, x in enumerate(primes) if x]


def factors_generator(x):
    primes = get_primes(x)

    def find_factors(n):
        """Return all prime factors of n and how often they occur.
        E.g. 4 returns (2,2), 100 returns (2,2) (5, 2).

        Keyword arguments:
        n -- int -- find all the prime factors and how often they occur for this number
        primes -- list of int -- optional, list of primes to speed up calculation
        if primes is not provided calculate primes in the function call
        """
        if n == 0:
            return []
        primes_factors = [prime for prime in primes if n % prime == 0]
        while True:
            trianglenew = n
            for prime in primes_factors:
                trianglenew = trianglenew / prime
            primes_factors.extend(
                [prime for prime in primes if trianglenew % prime == 0])
            if trianglenew == 1:
                break

        return [(prime, primes_factors.count(prime)) for prime in set(primes_factors) if prime != 1]
    return find_factors


def factors_generator2(x):
    primes = get_primes(x)

    def find_factors(n):
        """Return all prime factors of n and how often they occur.
        E.g. 4 returns (2,2), 100 returns (2,2) (5, 2).

        Keyword arguments:
        n -- int -- find all the prime factors and how often they occur for this number
        primes -- list of int -- optional, list of primes to speed up calculation
        if primes is not provided calculate primes in the function call
        """
        if n == 0:
            return []
        factors = []
        for prime in primes:
            while n % prime == 0 and n > 1:
                factors.append(prime)
                n = n  / prime

        return [(prime, factors.count(prime)) for prime in set(factors)]
    return find_factors


# timeit.timeit('factors_generator(1000)(1000)', 'from __main__ import factors_generator', number = 1000)

# timeit.timeit('factors_generator2(1000)(1000)', 'from __main__ import factors_generator2', number = 1000)



# print(timeit.timeit(factors_generator2(1000)(1000), number = 100))

# def divisor_generator(n, primes):
#     """Return all divisors of n as list.

#     Keyword arguments:
#     n -- int -- find all the divisors for this number
#     primes -- list of int -- optional, list of primes to speed up calculation
#     if primes is not provided calculate primes in the function call
#     """

#     if n == 1:
#         return [1]
#     factors = factor_generator(n, primes)
#     nfactors = len(factors)
#     f = [0] * nfactors
#     divisors = []
#     while True:
#         divisors.append(functools.reduce(lambda x, y: x*y,
#                                          [factors[x][0]**f[x] for x in range(nfactors)], 1))
#         i = 0
#         while True:
#             f[i] += 1
#             if f[i] <= factors[i][1]:
#                 break
#             f[i] = 0
#             i += 1
#             if i >= nfactors:
#                 return divisors


# def collatz_counter(n):
#     counter = 0
#     while True:

#         if n % 2 == 0:
#             n = int(n / 2)
#         else:
#             n = 3*n + 1
#         counter += 1
#         if n == 1:
#             break
#     return counter


# def logmap(r, x):
#     return r * x * (1 - x)


# def logmapite(r, x, n, cutoff):
#     i = 0
#     result = []
#     while True:
#         x = logmap(r=r, x=x)
#         result.append(x)
#         i += 1
#         if i == n:
#             break

#     result = [round(value, 6) for value in result]
#     result = list(set(result[cutoff:]))
#     df = pd.DataFrame(result, columns=["fixedpoint"])
#     df["r"] = r
#     return df


# def bifurcation(smallest, largest, step, x, n, cutoff):

#     scalingstep = int(step ** -1)
#     ranges = [
#         x * step for x in range(int(smallest * scalingstep), int(largest * scalingstep))]

#     df = pd.DataFrame()
#     for value in ranges:
#         df = pd.concat([df, logmapite(value, x, n, cutoff)])

#     df.plot.scatter("r", "fixedpoint")
#     return df


# def pascal(oldlist):
#     oldlist = [0] + oldlist + [0]
#     newlist = []
#     for i in range(len(oldlist) - 1):
#         newlist.append(oldlist[i] + oldlist[i+1])

#     return newlist


# for i in range(5, 10000):
#     b = sum(divisor_generator(i, primes)[:-1])

#     if b == 1 | b == i:
#         continue

#     a = sum(divisor_generator(b, primes)[:-1])

#     print(i)
#     if a == i:
#         result.append(i)