from abc import ABC, abstractmethod

class Shape(ABC):
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def calculate_area(self):
        return self.length*self.width

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def calculate_area(self):
        return 3.14*self.radius**2

r = Rectangle(10, 20)
c = Circle(10)  
print(r.calculate_area())
print(c.calculate_area())