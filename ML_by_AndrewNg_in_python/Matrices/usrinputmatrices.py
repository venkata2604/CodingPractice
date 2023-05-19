import numpy as np


A = np.array([[1, 2, 4],
              [5, 3, 2],
              [7, 8, 9]])


B = np.array([[1, 3, 4],
              [1, 1, 1],
              [2, 5, 7]])


multiply_1 = A*B
Multiply_2 = B*A
print(multiply_1, '\n', '\n', Multiply_2)

comparison = multiply_1 == Multiply_2
check = comparison.all()
print(check)

if check is True:
    print(" multiplication is commutative ")
else:
    print("multiplication is NOT commutative")
