# this below functions only help ful for the no.of arguements we provide in function. i.e 2 in this case.
def add(a,b):
    print("SUM OF TWO ELEMETS IS: ",a+b)

add(2,3)

# using *args -> can store multiple values and also it uses tuple to store it's values.

def addd(*args):   # *args uses tuple to store it's values
    total=0
    for ele in args:
        total+=ele
    return total

print("Using *args the sum is: ",addd(1,2,5))

#**kwagrs-> stores values in dictionary

def print_address(**kwargs): 
    for key,val in kwargs.items(): 
        print(f"{key}==> {val}")
        
print_address(street=" ABC STREET",city="UNKNOWN_CITY",state="NOBODY_KNOWS",zip=32541)
