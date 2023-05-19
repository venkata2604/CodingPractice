def gcd(n1, n2):
    maximum_number = max(n1, n2)
    for i in range(2, maximum_number):
        # print(i)
        if (n1 % i == 0) and (n2 % i == 0):
            temp = i
    final_gcd = temp
    return final_gcd


a = 60
b = 48

result = gcd(a, b)
print(result)

