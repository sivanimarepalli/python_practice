import math # to use the constant values that are available for us in this module.
friends=0
friends=friends+1 #addition or can sometimes be increment.
friends+=1 # sometimes += is known as a type of assignment operator.
print(friends) # prints 2 as output.

# SUBTRACTiON
frnds=5
frnds=frnds-1# subtracts 5-1 and stores 4 in the same variable.
frnds-=1 # also a type of assignment operator but performs the same operation as above.
print(frnds)

#multiplication
print(frnds*5) # multiplies the number in frnds variable to the value 5
frnds*=5 # assignment operator using multiplication.

# division
friends=10
friends=friends/2
friends/=2
print(friends)

# exponaentioal

print(5**2)

# remainder
print(frnds%2) # % returns remainder of the operation.

# BUILT_IN functions in python
print("BUILT-IN functions")
x=3.14
y1=-4
y=4
z=5
res=round(x)# it will return to it's nearer integer value
print(f" Result of round() is: {res}")

res=abs(y1)# it is the distance away from zero as awhole number
print(f"abs() is: {res}")
res=pow(4,3) # returns the 4^3 value which is 64
print(f"pow() is : {res}")
print("max is:",max(x,y,z))# returns the maximum value in the provided values.
print("min is:",min(x,y,z))# returns the minimum value in the provided values.

# after importing math module. use of constants,built-in functions,etc

print("pi val is: ",math.pi)
print("e val is: ",math.e)
result=math.sqrt(225) # returns the square root of 225
print(f"sqrt() is: {result}")
result=math.ceil(5.5)# returns the rounded up value of a floating num.
print(f"ciel() is :{result}")
result=math.floor(5.5)# returns the rounded down value of a floating num.
print(f"floor() is :{result}")