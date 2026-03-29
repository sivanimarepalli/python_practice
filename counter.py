# Write make_counter(start=0) that returns a function counter() which, each time it’s called, increments and returns the next value (1, 2, 3 … starting from start+1).
def make_counter(start=0):
    def counter():
        nonlocal start
        start+=1
        return start
    return counter

res=make_counter()
print(res())
