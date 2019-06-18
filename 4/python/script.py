int(str(123102)[::-1])

result = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        prod = i * j
        if int(str(prod)[::-1]) == int(prod) and prod > result:
            result = prod
            print(i, j, result)
