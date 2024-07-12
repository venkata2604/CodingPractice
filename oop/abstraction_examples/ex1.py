from abc import ABC, abstractmethod
import math

# abstract class called shape where we will define the properties of a shape such as area and perimeter
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# concrete class called rectangle where abstract methods are defined 
class Rectangle(Shape):

    #constructor
    def __init__(self, length, breadth):
        self.length = length 
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2*(self.length + self.breadth)
    

# concrete class for circle where abstract methods are defined
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius 

    def area(self):
        return (math.pi)*self.radius* self.radius
    
    def perimeter(self):
        return 2* math.pi * self.radius
    

if __name__ == "__main__":
    # Usage example
    rectangle = Rectangle(5, 4)
    print("Rectangle Area:", rectangle.area())         # Output: Rectangle Area: 20
    print("Rectangle Perimeter:", rectangle.perimeter())   # Output: Rectangle Perimeter: 18

    circle = Circle(3)
    print("Circle Area:", circle.area())               # Output: Circle Area: 28.26
    print("Circle Perimeter:", circle.perimeter())     # Output: Circle Perimeter: 18.84

    



