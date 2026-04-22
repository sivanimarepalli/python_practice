# Build make_accumulator(start=0) returning add(value) that adds value to an internal total and returns the new total.
def make_accumulator(start=0):
    total=start
    def add(value):
        nonlocal total
        total+=value
        return total
    return add

strt=make_accumulator(16)
print(strt(5))
print(strt(6))
print(strt(7))
print(strt(8))