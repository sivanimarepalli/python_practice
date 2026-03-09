temp=25
is_raining=False
if temp>35 or temp<0 or is_raining:
    print("The outdoor even is canceled")
else:
    print("The outdoor event is still scheduled")

    #AND
tmp=25
is_sunny=True
if tmp>=28 and is_sunny:
    print("It is sunny and hot outside")
elif tmp<=0 and is_sunny:
    print("It is cold outside")
elif tmp==25 and is_sunny:
    print("It is humid outside")
else:
    print("IT is raining outside")

# conditional expression
num=5
print("Positive" if num>0 else "Negative")
result= "Even" if num%2==0 else "Odd"
print(result)