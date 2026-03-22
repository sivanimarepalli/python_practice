# Given a list of tuples (item, category), create a dictionary grouping items under their category.
my_list=[("item1","A"),("item2","B"),("item3","A"),("item4","C"),("item5","C")]
my_dict={}
for tup in my_list:
    if tup[1] not in my_dict:
        my_dict[tup[1]]=[tup[0]]
    else:
        my_dict.get(tup[1]).append(tup[0])
print(my_dict)
