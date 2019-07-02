import math

def proper_divisors(n):
    result = []
    for i in range(1, math.ceil(n/2) + 1):
        if n%i == 0:
            result.append(i)
    return result

proper_divisors(100)

result = {}
for i in range(1, 10000):
    result[i] = sum(proper_divisors(i))



proper_divisors = []
divisors = []
for i in range(1, 10000):
    try:
        if i == result[result[i]] and result[i] != i:
            proper_divisors.append([result[i], result[result[i]]])
            divisors.append(result[i])
    except KeyError:
        print("keyerror")

print(sum(divisors))