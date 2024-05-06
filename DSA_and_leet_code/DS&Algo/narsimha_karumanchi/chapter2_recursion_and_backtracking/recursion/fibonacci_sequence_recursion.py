# fibonacci sequence is the sequence obtained by summing two previous numbers 
# so the numbers in sequence are 0,1,1,2,3,5,8,13,21,44,.... etc 

def fibonacci(n):
    if n <=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)


x= 4
if x>=0:
    for i in range(x):
        print(fibonacci(i), end = ' ')


"""
The time complexity of this algorithm is O(2^n). 

The calculation is as follows:
########### 
for the method "fibonacci(n)" the time complexity is O(2^n).
When a number is passed to the function, each number is split into two leaves of a binary tree. 
The first level of tree root contains f(n) which is the original supplied value. 
This root branches into two nodes f(n-1) and f(n-2). 
The terminal nodes are all the base conditions either f(0) or f(1).
Therefore starting from the root node we have 1 , 2, 4, 8, etc as the number of nodes at each level.
The number of nodes at the last level is equal to 2^n.
Hence, the time complexity is O(2^n)

##########
In the second part of the code where the function is called inside a loop, the number of times a loop executes 
is equal to the number of values in the range. Hence the time complexity is O(n). 

$$$$$$$$$$ 
Combining both of them, we have O(x*2^n). which is still equal to O(2^n)

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
The space complexity is O(n) as the function(n) keeps track of the value and stacks it till the end of function calls
"""


