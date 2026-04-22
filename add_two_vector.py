# Create a class Vector that overloads the + operator to add two vectors.
# Demonstrate adding Vector(1,2) and Vector(3,4).
class Vector:
    def __init__(self,l1,l2):
        self.l1=l1
        self.l2=l2
    def __add__(self,other):
        return Vector(self.l1+other.l1,self.l2+other.l2)
    def __str__(self):
        return f"{self.l1},{self.l2}"

v1=Vector(1,2)
v2=Vector(3,4)

print(v1+v2)