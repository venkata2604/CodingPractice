numbers = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9]
noduplicates = list()
print(numbers)
for i in numbers:
    if i not in noduplicates:
        noduplicates.append(i)
print(noduplicates)