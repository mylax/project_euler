from funcs import fibonacci
print(sum(i for i in fibonacci(4000000) if i % 2 == 0))

