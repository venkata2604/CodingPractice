x= input("Phone:")
#print(x)
y = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine",
    "0" : "Zero"
}

output = ""

for i in x:
    #print(y)
    #print(y.get(i, "value not in dictionary")) # if we leave it here we get words in different lines, to get in same line, do string concatenation
    output += y.get(i, "value not in dictionary")+ " "
print(output)

