def hello_decorator(func):
    def inner1(*args, **kwargs):
        print("before execution")
        breakpoint()

        # getting the returned value
        returned_value = func(*args, **kwargs)
        print("after Execution")

        # returning the value to the original frame
        return returned_value

    return inner1


# adding the decorater to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("inside the function sum 2 nums")
    return a + b


n1, n2 = 1, 2

# getting the value through return of the function

print("sum = ", sum_two_numbers(n1, n2))
