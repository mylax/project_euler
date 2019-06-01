def find_multiples_generator(k):
    """
    returns a function which generates all multiples k of any number passed to it

    @param k: return function which returns all multiples k
    """
    return lambda n: [n for n in range(1, n) if n % k == 0]
  

def find_multiples(k, n):
    """
    returns all multiples in list k of n, up to n 
    """
    multiples = []
    for divisor in k:
        multiples += find_multiples_generator(divisor)(n)
    combined_list = list(set(multiples))
    combined_list.sort()
    return combined_list

