# Note: method overloading is not supported in python
# A class derived from abc is called abstract class in py
# Abstract class can have abstract and concrete methods
# Abstract class methods need to be implemented
# One cant create an instance for abstract class
# It is not necessary that every method in an abstract class in an abstract method
# if there is any method in a class that is abstract then that class must be abstract

from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        self.id = 101
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def peri(self):
        pass

    def __lt__(self, other):
        if self.area()>other.area():
            return True
        else:
            return False
        

class Rect(Shape):
    def __init__(self, a, b):
        super().__init__()
        self.a =a
        self.b =b

    def area(self):
        return self.a*self.b

    def peri(self):
        return (self.a+self.b)*2
    
class Square(Shape):
    def __init__(self, a):
        super().__init__()
        self.a =a
        self.b =a

    def area(self):
        return self.a*self.b

    def peri(self):
        return (self.a+self.b)*2
    
r = Rect(10, 20)
s = Square(20)
print(r.area())  # Output: 200
print(r.peri())  # Output: 60
print(s.area())  # Output: 400
print(s.peri())  # Output: 60
print(Rect.mro())
print(r>s)
