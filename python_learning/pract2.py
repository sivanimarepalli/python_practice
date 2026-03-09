#1. To print circumference of a circle. we are using pi constant from math module.
import math
radius=float(input("Enter the radius of a circle"))
cir=2*math.pi*radius
print(f"The circumference of a circle is: {round(cir,2)} cm") #it will make the output to only have 2 numbers after the decimal 
# 2. To Print the area of a circle.
radi=float(input("Enter the radius of circle"))
area=math.pi*pow(radi,2)
print(f"The area of the circle is {area}")
# 3. Identifying the hypotenus of the right angle triangle
a=float(input("Enter the side A of a triangle: "))
b=float(input("Enter the side b of the triangle: "))
c=math.sqrt(pow(a,2)+pow(b,2))
print(f"The hypoteneous of the triangle is{round(c,2)}")