# dunder methods are special methods in a class which are called during python operations
'''
Other dunder methods
1. __str__(): This method is called when we use print() function on an object.
2. __repr__(): This method is called when we use repr() function on an object.
3. __len__(): This method is called when we use len() function on an object.
4. __getitem__(): This method is called when we use indexing on an object.
5. __setitem__(): This method is called when we use assignment on an object.
6. __delitem__(): This method is called when we use del statement on an object.
7. __iter__(): This method is called when we use for loop on an object.
8. __next__(): This method is called when we use next() function on an object.
9. __reversed__(): This method is called when we use reversed() function on an object
10. __eq__(): This method is called when we use == operator on an object.
12. __add__(): This method is called when we use + operator on an object.
13. __sub__(): This method is called when we use - operator on an object.
14. __mul__(): This method is called when we use * operator on an object.
15. __truediv__(): This method is called when we use / operator on an object
'''

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __add__(self, other):
        return Fraction(self.numerator + other.numerator, self.denominator+other.denominator)
    
a = Fraction(1,5)
b = Fraction(5,5)
c = a+b
print(c)
print(r"\/\//\\\d")