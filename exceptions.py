# A programmer should see that his program should not crash. if unsupported input is given three should be a way to convey it to user
try:
    age = int(input('age:'))
    income = 20000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print("Age cannot be Zero")
except ValueError: # this is only catching value type error
    print('Invalid Input')
#exit code 0 means no error
#exit code 1 means there is error
