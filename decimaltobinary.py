binary_list = []
dnum = int(input("Enter the decimal Number: "))
print(f"The number you entered is : {dnum}")
while dnum != 0:
    rem = dnum % 2
    binary_list = [rem] + binary_list
    dnum = int(dnum/2)
    print("dnum", dnum)
print("BINARY: ", *binary_list)

