name="Sivani"
language='Python'
days=1
print(name," Has started learning the programming language",language,"from the following days",days)
print(f"{name} has started learning the programming language {language}from the following days{days}")# f-string


#integer
age=20
print(f"{name} is {age} years old")

#Float

price=99.55
print(F"the product that you bought can be purchased at {price} rupees as well")

#Boolean

is_student=True
print(f"Are you a student?: {is_student}")


#Type Casting

myname="Sivani"
myage=20
gpa=8.7
is_studentt=True
print(type(myname)) #type()--> returns the data type of a variable
print(type(myage))
print(type(gpa))
print(type(is_studentt))
#typecasting the above variables
gpa=int(gpa)
print(gpa)
print(type(gpa))
myname=bool(myname)
print(myname)#returns true as the myname variable contains a value. if it doesn't have a value then it will return false