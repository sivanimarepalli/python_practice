class Car:
    # helps to create an object (dunder=>double underscore)
    def __init__(self,model,year,color,for_sale): 
        self.model=model
        self.year=year
        self.color=color
        self.for_sale=for_sale
    def drive(self):
        print("You drive a car")
    def stop(self):
        print("You stop the car")
#obj1
car1=Car("Mustang",2024,"red",False) # object creation
print(car1) # prints the memory address of the car1 object
# to access it's attributes use syn: obj_name.attr_name
print("CAR OBJECT-1: ")
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)
# function accessing
car1.drive() 
car1.stop()
#obj2
car2= Car("corvette",2025,"blue",True)
print("CAR OBJECT-2: ")
print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)


# methods are actions that perform in a class
car2.drive()
car2.stop()