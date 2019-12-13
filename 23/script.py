import math



def table_sums(elements, n):
    elem_len = len(elements)
    subset=([[False for i in range(n+1)] for i in range(elem_len+1)])

    for i in range(elem_len+1):
        subset[i][0] = True

    for i in range(1,n+1):
        subset[0][i]=False

    for i in range(1,elem_len+1):
        for j in range(1,n+1):
            if j<elements[i-1]:
                subset[i][j] = subset[i-1][j]
            if j>=elements[i-1]:
                subset[i][j] = (subset[i-1][j] or subset[i - 1][j-elements[i-1]])

    return subset


def printSubsetsRec(elements, i, n, p, dp, result):
    if i == 0 and n != 0 and dp[1][n]:
        p.append(elements[0])
        result.append(p)
        return "done"
    if i == 0 and n == 0:
        result.append(p)
        return "done"
    if i == 0 and n != 0:
        return "done"

    if dp[i][n]:
        b = p.copy()
        printSubsetsRec(elements, i-1, n, b, dp, result)
    if n >= elements[i] and dp[i][n-elements[i]]:
        p.append(elements[i])
        printSubsetsRec(elements, i-1, n-elements[i], p, dp, result)

def find_combinations_sum(elements, n):
    table_2d = table_sums(elements, n)
    p = []
    result = []
    printSubsetsRec(elements, len(elements) - 1, n, p, table_2d, result)
    return result

def proper_divisors(n):
    result = []
    for i in range(1, math.ceil(n/2) + 1):
        if n%i == 0:
            result.append(i)
    return result

abundant = []
for i in range(1, 28123):
    if i < sum(proper_divisors(i)):
        abundant.append(i)

not_sum_abundant = []
for i in range(1, 28123):
    print(i)
    if not [x for x in find_combinations_sum(abundant, i) if len(x) == 2]:
        continue
    else:
        not_sum_abundant.append(i)