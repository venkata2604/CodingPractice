numbers = [3, 10, 65, 99, 101, 3, 2, 1, 0, 9, 8, 7]
max = numbers[0]
for number in numbers:
    print(number)
    if number > max:
        max = number
print("largest", max)
