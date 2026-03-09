fruits=["apple","banana","orange","grapes"] # it is a 1d lsit
vegetables=["tomato","potato","cabbage","spinach"] # it is a 1d lsit
meats=["chicken","fish","turkey"] # it is a 1d lsit

groceries=[fruits,vegetables,meats] # it is also a 1d list. But it stores another 1d list as values

# to print from a 1d list 
print(fruits)
# to change a value in a 1d list
fruits[0]="pineapple"

# but to print 2d list 
print(groceries) # displays all lists in one single line
# to print each list inside this groceries we use indexing.
# to print fruits list it is 
print(groceries[0])
# index 0: fruits
# index 1: vegetables
# index 2: meats
# to print element inside a list like for eg: fruits[0] from groceries
print(groceries[0][0]) # like a 2d array in cpp
print(groceries[1][0]) # from vegetables list

# to print everything in a 2d list use for loop as follows
for ele in groceries:
    print(ele)
# to access the elements inside the list in groceries use nested loops
for collection in groceries:
    for food in collection: 
        print(food,end=" ")
    print()

# a list can also contains collection of tuples
# or a tuple can contain a collection of sets like 2d list