class Shape:
    def __init__(self,color,filled):
        self.color=color
        self.filled=filled
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.filled else 'not filled'}")
class Circle(Shape):
    def __init__(self,color,filled,radius):
        super().__init__(color,filled) # enables  us to access parent class methods and variables
        self.color=color
        self.filled=filled
        self.radius=radius
    def describe(self):  # method overriding. if a function is present at both parent and child classes then the child class method will override the parent class one
        print(f"It is a circle with an area of{3.14*self.radius}")
class Square(Shape):
    def __init__(self,color,filled,width):
        super().__init__(color,filled)
        self.color=color
        self.filled=filled
        self.width=width
class Triangle(Shape):
    def __init__(self,color,filled,width,height):
        super().__init__(color,filled)
        self.color=color
        self.filled=filled
        self.width=width
        self.height=height

circle =Circle("red",True,5)
print(circle.color)
print(circle.filled)
print(circle.radius)

sqr=Square("pink",False,5)
print(sqr.color)
print(sqr.filled)
print(sqr.width)
sqr.describe()
circle.describe()