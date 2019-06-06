def find_multiples(k, n):
    """
    returns iterator of all multiples of k in n, up to n
    not ordered
    """
    seen = set()
    for item in (l for i in k for l in range(i, n, i)):
        if item not in seen:
            seen.add(item)
            yield(item)

