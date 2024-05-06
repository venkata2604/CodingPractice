def factorial(n):
    if n==0:
        return 1
    result = 1
    while n>1:
        result = result*n
        n -=1
    return result

print(factorial(5))
    

"""
The time complexity for this code is O(n)
"""