# Merge two inventory dicts by summing quantities of same keys.
dict1={"Apple":1,"Ball":5,"Cat":6}
dict2={"Apple":2,"Ball":3,"Cat":4}
dict3={}
for key,val in dict1.items():
    if key in dict3:
        dict3[key]=val
    else:
        dict3[key]=val
for keys,vals in dict2.items():
    if keys in dict3:
        dict3[keys]=vals
    else:
        dict3[keys]=vals
print(dict3)

