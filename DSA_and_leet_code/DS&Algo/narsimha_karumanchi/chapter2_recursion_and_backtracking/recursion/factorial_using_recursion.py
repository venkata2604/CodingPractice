# Factorial of a number 3! = 3x2x1 = 6
def factorial(number):
    if number ==0:
        return 1
    return number*factorial(number-1)

print(factorial(10))