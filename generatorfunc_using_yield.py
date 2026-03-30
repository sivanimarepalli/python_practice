# Write a generator function count_up_to(n) that yields numbers from 1 to n.
def count_up_to(n):
    for i in range(1,n+1):
        yield i

n=int(input("Enter an n value: "))
res=count_up_to(n)
for ele in res:
    print(ele)