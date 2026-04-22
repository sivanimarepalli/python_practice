# "Create classes Vehicle → Car → ElectricCar.
# Add attributes and methods at each level.
# Show how ElectricCar can access methods from Vehicle."
class Vehical:
    def __init__(self,name):
        self.name=name
    def data(self):
        print(f"The name of the vehical is {self.name}")
class Car(Vehical):
    def __init__(self,name,speed):
        self.speed=speed
        super().__init__(name)
    def details(self):
        super().data()
        print(f"The vehical {self.name} has a speed of {self.speed}kmph")
class electricCar(Car):
    def __init__(self,name,speed,color):
        self.color=color
        super().__init__(name,speed)
    def property(self):
        super().details()
        print(f"The vehical {self.name} has a speed of {self.speed} kmph and it's color is {self.color}")
ec=electricCar("car",200,"Pink")
ec.property()