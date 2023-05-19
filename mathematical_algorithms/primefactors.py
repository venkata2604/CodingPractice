import math

# number = 64


def prime_factors(number):
    while number % 2 == 0:
        print("2")
        number = number/2
    for i in range(3, int(math.sqrt(number))+1, 2):
        while number % i == 0:
            print(i)
            number = number/i
            # print("end", number)
    if number > 2:
        print(number)


n = 21
prime_factors(n)
