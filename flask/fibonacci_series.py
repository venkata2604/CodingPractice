# write a fibonacci series program in python

def fibonacci_series(n):
    if n <= 1:
        return n
    else:
        return fibonacci_series(n-1) + fibonacci_series(n-2)
    
nterms = int(input("Enter the number of terms: "))
if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(fibonacci_series(i))

# Output:
# Enter the number of terms: 10
# Fibonacci sequence:
# 0
# 1
