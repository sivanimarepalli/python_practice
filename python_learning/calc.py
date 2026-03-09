#calculator
operator=input("Enter an operator to perform an operation: ")
num1=int(input("Enter the 1st number: "))
num2=int(input("Enter the 2nd number: "))
if operator=="+":
    res=num1+num2
elif operator=="-":
    res=num1-num2
elif operator=="*":
    res=num1*num2
elif operator=="/":
    res=num1/num2
else:
    print("The operator is not +,/,-,* please enter any of the four")
print(res)