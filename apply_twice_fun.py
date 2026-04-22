#  Write a function apply_twice(func, x) that takes another function func and a value x, then returns func(func(x)).
def apply_twice(add,x):
    return add(add(x))
def square(x):
    return x**2
squarez=apply_twice(square,5)
print(squarez)
    
