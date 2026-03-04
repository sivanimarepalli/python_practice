num=int(input("Enter a number: "))
org=num
s=0
while num>0:
    d=num%10
    s+=d
    num//=10
print(f"Sum of digits in {org} is {s}")