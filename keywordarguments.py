# container of few lines of code which perform a specific task
def greet_user(first_name, last_name):
    print(f'hi {first_name} {last_name} there')
    print("welcome aboard\n")


print("Start")
greet_user(last_name="lisa", first_name="vicari")# first use positional arguments if any, then only use keyword arguments

# we are calling the already defined function
greet_user("anushka", "shetty")
print("finish")
# parameters are place holders for arguments
#arguments are actual pieces of information
