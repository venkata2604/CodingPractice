A = []

n=int(input("Enter n for n x n matrix : "))    #3 here
#use list for storing 2D array
#get the user input and store it in list (here IN : 1 to 9)
print("Enter the element ::>")
for i in range(n):
   row = []                                      #temporary list to store the row
   print("enter the values for ", i+1, "st row")
   for j in range(n):
      row.append(int(input()))                   #add the input to row list
   A.append(row)                                 #add the row to the list

print(A)

