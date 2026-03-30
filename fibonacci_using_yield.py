# Write a generator that yields the first n Fibonacci numbers.
def fib(n):
    a,b=1,1
    for i in range(n):
        yield a
        a,b=b,a+b

n=int(input("Enter a n value: "))

r=fib(n)
for ele in r:
    print(ele)