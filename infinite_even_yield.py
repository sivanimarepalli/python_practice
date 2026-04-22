# Create a generator infinite_even() that yields even numbers indefinitely.
def infinite_even():
    i=0
    while True:
        yield i
        i+=2
    
res=infinite_even()
for i in res:
    print(i)