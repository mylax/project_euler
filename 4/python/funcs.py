def is_palindromic(n):
    return n == int(str(n)[::-1])

def find_palindromic(n1, n2):
    '''
    finds highest product of two numbers that is palindromic in range of 1 to n1
    and 1 to n2
   '''
    result = 0
    for i in range(n1+1):
       for j in range(n2+1):
           prod = i*j
           if is_palindromic(prod) and prod > result:
               result = i * j
               first_n = i
               second_n = j
    return {"prod":result, "n1":first_n, "n2":second_n}