# Build counter() that returns a function next() which, when called, returns 1, 2, 3, … without using globals.
def counter():
    count=0
    def next():
        nonlocal count
        count+=1
        return count
    return next

count=counter()
print(count())
print(count())
print(count())