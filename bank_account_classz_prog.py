# Create a class BankAccount with a private attribute __balance.
# Add methods deposit() and withdraw() to modify balance.
# Show how to access balance safely using a getter.
class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
        return self.__balance
    def withdraw(self,amount):
        if amount>self.__balance:
            print("insufficient balance.")
        elif amount <=0:
            print("Number must be greater than 0")
        else:
            self.__balance-=amount
        return self.__balance
    def get_balance(self):
        return self.__balance

ba1=BankAccount(25000)
print(ba1.deposit(25000))
print(ba1.withdraw(5000000))
print(ba1.get_balance())

