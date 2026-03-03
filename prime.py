num=int(input("Enter a number to check: "))
if num<=1:
    print(f"{num} is not prime")
else:
    is_prime=True
    
    for i in range(2,num):
        if num%i==0:
            is_prime= False
            break
if is_prime:
    print(f"{num} is Prime")
else:
    print(f"{num} is not prime")