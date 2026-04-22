# Implement make_multiplier(k) that returns a function multiplying its input by k.
def make_multiplier(k):
    def multiply(num):
        return num*k
    return multiply
multiplication=make_multiplier(2)
print(multiplication(8))