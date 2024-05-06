def is_palindrome(num):
    return str(num) == str(num)[::-1]

num = int(input("Enter a number: "))
if is_palindrome(num):
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")