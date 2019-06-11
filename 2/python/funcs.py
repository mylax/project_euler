def fibonacci(limit):
    i = 0
    j = 1
    while(i <= limit):
        yield(i)
        j, i = i + j, j