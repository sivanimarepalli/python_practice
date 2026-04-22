# Write a function that determines if an integer n is a power of two using bitwise operations.
# Hint: A number is a power of two if n > 0 and (n & (n - 1)) == 0.
# Example:
# Input: n = 16 → Output: True.
def power_of_two(n):
    if n<=0:
        return False
    else:
        return (n&(n-1))==0

n=int(input("Enter a number: "))
print(power_of_two(n))