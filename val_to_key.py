# Given a dict and a target value, return all keys mapping to that value.
my_dict={1:"apple",2:"bat",3:"cat",4:"dog",5:"eagle"}
target=input("Enter the target to find key for: ").lower()
res=[]
for key,val in my_dict.items():
    if val==target:
        res.append(key)
print(res)