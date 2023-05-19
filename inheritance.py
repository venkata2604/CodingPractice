# inheritance is mechanism for reusing code
class Mammals:
    def walk(self):
        print("walk")


class Dog(Mammals):
    pass # python interpreter doesn't like empty classes. So, we write pass


class Cat(Mammals):
    pass


dog1 = Dog()
dog1.walk()
