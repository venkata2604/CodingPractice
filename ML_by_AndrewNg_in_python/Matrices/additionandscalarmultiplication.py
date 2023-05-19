#  initialising matrix A and B
import numpy as np

A=[]

r = int(input("enter the number of rows for matrix:"))
c = int(input("enter number of coloumns for matrix:"))



A = np.array([[1, 2, 4],
              [5, 3, 2],
              [7, 8, 9]])
B = np.array([[1, 3, 4],
             [1, 1, 1],
             [2, 5, 7]])
#  print(A)
#  print(B)
#  initialising a constant s
s = 2

# element wise addition
add_AB = A+B
print("Addition of Matrices A and B \n", add_AB)

#  element wise subtraction
subtract_AB = A-B
print("Subtraction of Matrices A and B  \n", subtract_AB)

# Matrix Matrix multiplication
m_multiplication = A*B
print("Multiplication of Matrices A and B \n", m_multiplication)

#  scalar multiplication
multiplication_A = A*s
print("Multiplication of Matrix A with Scalar s \n", multiplication_A)

#  scalar Division
division_A = A/s
print("Division of Matrix A with Scalar s \n", division_A)

# scalar addition
s_addition_A = A+s
print("Addition of Matrix A with Scalar s \n", s_addition_A)


# a vector of 3X1
v = ([1],
     [1],
     [1])

# matrix and vector Multiplication
va = A*v
print("Multiplication of Matrix and vector \n", va)

# attaining a transpose of matrix
print(" Transpose of A \n", np.transpose(A))
print(" Transpose of B \n", np.transpose(B))
