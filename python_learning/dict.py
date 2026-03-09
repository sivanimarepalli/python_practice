#dictionary that store {key:value}pairs
capitals={"USA":"Washington D.C.",  
          "India":"New Delhi",
          "China":"Beijing",
          "Russia":"Moscow"}
# print(dir(capitals)) # displays all the methods available in dictionary
# print(help(capitals))# prints the descriptions for the methods available in dictionary
print(capitals.get("USA"))# prints the value of usa i.e washington dc. if that value is not there it will return none
capitals.update({"Germany":"Berlin"}) #adds anew key-value pair to the existing dictionary or update an "already existing value to a particular key"
print(capitals)
capitals.pop("China")# removes the element china and it's corresponding value from dictionary
capitals.popitem()# removes the latest value that was added.
#capitals.clear()# clears the dictionary 
print(capitals.keys())#to obtain only keys from a dictionary but not values 
# for loop to iterate through the keys in dictionary
for key in capitals.keys():
    print(key)
print(capitals.values())# to obtain the values from the dictionary not keys
# for loop to iterate through the values in dictionary
for value in capitals.values():
    print(value)
print(capitals.items())# it returns a dictionary object which resembles a 2-D list of tuples
for key,value in capitals.items():
    print(f"{key}:{value}") # returns the entire dictionary