class Animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    pass
class Cat(Animal):
    pass
class Mouse(Animal):
    pass
dog=Dog("Sheero")
cat=Cat("snowbell")
mouse=Mouse("stuart")
dog.eat()
dog.sleep()
cat.eat()
cat.sleep()
mouse.eat()
mouse.sleep()
print(cat.name)