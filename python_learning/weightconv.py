# weight conversion program
weight=float(input("Enter your weight: "))
unit=input("Kilograms or pounds? (K/P): ")
if unit=="K":
    weight=weight*2.205
    unit="Lbs."
    print(f"The weight is :{round(weight,2)}{unit}")
elif unit=="P":
    weight=weight/2.205
    unit="Kgs."
    print(f"The weight is :{round(weight,2)}{unit}")
else:
    print("Incorrect unit entered")