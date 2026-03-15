# Division that returns "NaN" if denominator is zero
def division(x,y=0):
    return x/y

x=int(input("Enter a number: "))
y=int(input("Enter another number: "))
if y==0:
    print("NAN")
else:
    print(f"The division of {x} and {y} is: {division(x,y)}")