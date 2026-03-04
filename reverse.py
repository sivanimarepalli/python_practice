num=int(input("Enter a number to reverse: "))
rev=0
while num>0:
    d=num%10
    rev=d+rev*10
    num//=10
print(f"Reversed number is {rev}")