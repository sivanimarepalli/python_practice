#list
fruits=["apple","mango","banana"] # list can store more values seperated by commas
print(fruits)# prints all elements in the list
print(fruits[2])# indexing prints the value at index 2
print(fruits[::2])#slicing it prints every second element
for x in fruits: # to iterate through the list and to print them.
    print(x)
# methods to use on list
#print(dir(fruits)) # displays all the methods that we can perform on lists
if "apple" in fruits:
    print("YEAHHHH!!!")
else:
    print("NOOOOOOO!")

# append-> add an element at the end of the list syn: list_name.append("ELE")
#remove-> removes an element syn: list_name.remove("ELE_NAME")
# insert-> adds an element at a particular index syn: list_name.insert(index,"ele_name")
# sort-> sorts an list syn: list_name.sort()
# reverse-> reverses a list syn: list_name.reverse()
# clear-> clears the entire list syn: list_name.clear()
#index -> to identify an element at a particular index syn: list_name.index("ele")
# count-> to count the no.of times an element has been repeated syn: list_name.count()

#set
print("COLLECTIONS: SET")
froots={"mango","orange","grapes","strawberry"}
print(f"SET VALUES: {froots}")
#print(dir(froots)) # to display all the different methods and functions available
#print(help(froots)) # to display all the descriptions of the methods available for set
# len(set_name)-> returns the length of the set.

# we can use "in" operator to identify if a value is in set just like we did in list
# we can't use indexing on a set
#add()-> adds a new element in to the set syn: set_name.add(ele)
# remove()-> removes an element in the set syn: set_name.remove(ele)
# pop()-> removes the first elements syn: set_name.pop()
# clear()-> clears the entire set syn: set_name.clear()


# Tuple
print("COLLECTION: TUPLE")
frouts=("apple","gauva","grapes","orange")
print(f"tuple: {frouts}")
# we can also use the dir() function to display the available methods in tuple.
# we can also use help() function to display descriptions
# len(tup_name) -> to display the length of the tuple
# can also use "in" operator just like we did previously
# index("ele")->  returns the index of ele provided syn: tup_name.index(ele_name)
# count("ele")-> returns the count of the ele provided syn: tup_name.count(ele_name) 