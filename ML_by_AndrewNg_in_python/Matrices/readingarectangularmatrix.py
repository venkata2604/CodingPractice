A = []

r = int(input("enter the number of rows:"))
c = int(input("enter the number of columns"))

print("size of matrix =", r, "X", c)

# use list for storing 2D array

# get the user input and store it in list (here IN : 1 to 9)


print("Enter the elements row wise >")
for i in range(r):
    row =[]
    # print('enter the values for', i+1, 'row')
    j = 0
    for j in range(c):
        print('enter the values for', i + 1, 'row and ', j+1, 'column')
        row.append(int(input()))
    A.append(row)
for k in A:
    print(k)

print(A)

# for i in range(r):
#    row = []                                      #temporary list to store the row
#    print("enter the values for ", i+1, "st row")
#    for j in range(c):
#       row.append(int(input()))
#   A.append(row)


