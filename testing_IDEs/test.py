# write a python code to print 10 fibonacci numbers
import datetime

start = datetime.datetime.now()

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
for i in range(40):
    print(fib(i))

end = datetime.datetime.now()
print(end - start)