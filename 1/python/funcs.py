def find_multiples(k, n):
    """
    returns all multiples of k in n, up to n
    """
    multiples = []
    for divisor in k:
        multiples += list(range(divisor, n, divisor))
    combined_list = list(set(multiples))
    combined_list.sort()
    return combined_list

