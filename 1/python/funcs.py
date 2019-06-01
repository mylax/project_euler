def find_multiples_generator(k):
    """
    returns a function that itself returns a list of all multiples k up to the number n
    """
    def find_multiples(n):
        return [n for n in range(1, n) if n % k == 0]

    return find_multiples    


def find_multiples_3_or_5(n):
    multiples_three = find_multiples_generator(3)(n)
    multiples_five = find_multiples_generator(5)(n)
    combined_list = list(set(multiples_three + multiples_five))
    combined_list.sort()
    return combined_list

