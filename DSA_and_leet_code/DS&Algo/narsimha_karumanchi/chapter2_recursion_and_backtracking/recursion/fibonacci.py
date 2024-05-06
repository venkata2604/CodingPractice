def fibonacci(n):
    """
    n is the number of terms required in the fibonacci
    """
    n1 = 0
    n2 = 1
    lst = []
    lst.extend([n1, n2])
    # print(lst)

    for i in range(n-2):
        # print(i)
        next_term = lst[i]+lst[i+1]
        lst.append(next_term)
    return list(lst[:n])

print(j for j in list(fibonacci(4)))



