num=int(input("Enter a number: "))
n=1
for i in range(0,num):
    for j in range(0,i):
        print(n,end=" ")
    n+=1
    print()