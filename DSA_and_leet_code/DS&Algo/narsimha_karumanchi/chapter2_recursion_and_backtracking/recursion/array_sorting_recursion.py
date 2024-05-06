def isArrayInSortedOrder(A):
    # Base case
    if len(A) == 1:
        return True
    # Recursive case for recursion
    return A[0] <= A[1] and isArrayInSortedOrder(A[1:])
# A = [127, 220, 246, 277, 321, 454, 534, 565, 933]
A = [1,2,3, 4, 5, 6, 7, 8]
print(isArrayInSortedOrder(A))

"""
The function isArrayInSortedOrder is called on an array. The base case checks if the array has only one element. 
If there is only one element, it's obvious that the list has no other elements to be compared to and is sorted.
For the recursive csae, the list is taken as the first two elements of the list are compared. 
The code return A[0] <= A[1] returns either true or false based on the truth of condition. The second part,
where the function is called goes and calls the function again as there is and between two statements if checks 
logical and and returns true if all of the conditions are true and only true. 

###############################################################################################
The time complexity of this algorithms is O(n). The space complexity of this algorithm is O(n).
where n is the length of input array.

if the length of array is greater than 1, then the function calls itself with the rest of array except the first
one. This means that the function will be called n times, where n is the length of array. At each recursive call,
the function compares the first two elements of the array to check if they are in non-decreasing order.
This comparison takes constant time, so the total time taken by the function is proportional to the length of array. 

"""