from funcs import find_prime_factors



prod = 1
for key, val in find_prime_factors(list(range(11, 21))).items():
    prod *= key ** val

print(prod)