# def fun1():
#     a=1 # local variable in fun1(). cannot be accesed elsewhere not even in fun2()
#     print(a)
# def fun2():
#     b=2  # local variable in fun2(). cannot be accesed elsewhere not even in fun1()
#     print(b)
# fun1()
# fun2()

# function inside a function (ENCLOSED and LOCAL)
# def fun1():
#     x=1
#     def fun2():
#         x=2 # if we remove the x=2 in fun2() then the x=1 in fun1() will be printed as it is enclosed scope
#         print(x) # the x=2 overrides the x=1 and prints 2 as output. as local variables have high scope resolution
#     fun2()
# fun1()

# GLOBAL SCOPE

# def fun1():
#     print(x)
# def fun2():
#     print(x)

# x=5 # global variables

# fun1()
# fun2()

# BUILT-IN
from math import e
def fun1():
    print(e)

e=5 # overrides the built-in value in the module as it is global
fun1()