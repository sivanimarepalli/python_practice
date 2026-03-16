class Employee:
    count=0
    def __init__(self,name,position):
        self.name=name
        self.position=position
        Employee.count+=1
        # instance method
    def get_info(self):
        return f"{self.name} = {self.position}"
    @staticmethod
    def is_valid_position(position): # for a static method no need to create a object of the class
        valid_positions=["Manager","Cashier","Cook","Janitor"]
        return position in valid_positions
    @classmethod
    def get_count(cls):
        return f"Total no.of employees are: {cls.count}"

employee1=Employee("sivani","Manager")
employee2=Employee("doremon","Cook")
print(employee1.get_info())
print(Employee.is_valid_position("Cook"))
print(Employee.get_count())