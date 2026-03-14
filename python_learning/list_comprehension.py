doubles=[]
for x in range(1,11):
    doubles.append(x*2)

print(doubles)

# list comprehension:
print("LIST COMPREHENSION: ")
doublez=[x * 2 for x in range(1,11)]
print("doubles using list_comprehension:",doublez)
triples=[y*3 for y in range(1,11)]
print("triples using list_comprehension:",triples)
squares=[z*z for z in range(1,11)]
print("squares using list_comprehension:",squares)

# list comprehension using string:
fruits=["apple","orange","banana","coconut"]
upper_fruits=[ch.upper() for ch in fruits]
print("fruits in upper case: ", upper_fruits)

# list comprehension using if conditions as well
numbers=[-1,-2,9,5,4,6,7,-6,-5,-4,0]
neg_nums=[num for num in numbers if num<0]
pos_nums=[nums for nums in numbers if nums>=0]
print("positive numbers are: ",pos_nums)
print("negative numbers are: ",neg_nums)

# exercise:
grades=[85,42,79,90,56,61,30]
passing_grades=[grade for grade in grades if grade>=60]
print(f"THE PASSING GRADES ARE: {passing_grades}")
