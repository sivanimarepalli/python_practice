age=int(input("Enter your age: "))
if age>=18:
    print("You are eligible to vote")
elif age<0:
    print("You are not born YET!")

else:
    print("You are not eligible yet!!!")

#conditional operators
response=input("Would you like food? (Y/N): ")
if response=="Y":
    print("Have some food")
else:
    print("No food for you")
