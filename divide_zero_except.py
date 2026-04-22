# Iterate through a list of numbers and divide 100 by each. Handle division by zero without breaking the loop.
nums=[0,1,54,8,7,6,5]
for ele in nums:
    try:
        print(100//ele)
    except ZeroDivisionError as z:
        print(z)
