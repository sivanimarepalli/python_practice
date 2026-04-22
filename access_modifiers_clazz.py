# Create a base class with a protected attribute _salary and a private attribute __bonus.
# Show how subclasses can access _salary but not __bonus directly.
class Amount:
    def __init__(self,salary,bonus):
        self._salary=salary
        self.__bonus=bonus
    def data(self):
        print(f"Salary of employee is {self._salary} and Bonus for the employee is {self.__bonus}")
class Emp(Amount):
    def __init__(self,salary,bonus):
        super().__init__(salary,bonus)
    def amount_data(self):
        print(f"The salary is {self._salary}")
        print(f" the bonus is {self.__bonus}") # to access the private val use name mangling trick as self._Amount__bonus

e=Emp(500000,25666)
Amount.data(e)
e.amount_data()