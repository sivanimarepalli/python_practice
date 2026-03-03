num=int(input("Enter your number"))
org=num
c=len(str(num))
s=0
while num>0:
    d=num%10
    s+=(d**c)
    num//=10
if s==org:
    print(f"{org} is an armstrong number")
else:
    print(f"{org} is not an armstrong number")