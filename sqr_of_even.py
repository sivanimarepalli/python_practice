#From a list of numbers, return a list containing squares of only the even numbers.
nums=[1,5,6,4,7,8,23,44]
ev_sqr=[num**2 for num in nums if num%2==0]
print(f"squares of even nums: {ev_sqr}")