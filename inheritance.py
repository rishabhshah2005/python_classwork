class A:
    def __init__(self, a):
        self.a = a
    
    def getA(self):
        print(self.a)

class B(A):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b
    
    def getAB(self):
        super().getA()
        print(self.b)


b = B(5,10)
b.getAB()
b.getA()

# method resolution order based on C3 linearization algorithm starting from Python3
# Algorithm defines the MRO 
# 1 --> Take head of the list
# 2 --> If the head is not the tail of any other list, the added to the linearization of C and remove
#       it from the list 
# 3 --> Otherwise look the look the head of the other list and take it on the base of the above condition
# 4 --> repeat the operation until all classes are removed 

