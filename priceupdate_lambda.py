# Create a Price Update Pipeline (map → filter → reduce), give n list of product prices, apply 10% discount,  keep only items ≥ ₹200 after discount and compute the final bill total.
from functools import reduce
products=[150,25,258,360,46]
res=map(lambda x:x*0.9,products)
res=filter(lambda x:x>=200,res)
tot=reduce(lambda x,y:x+y,res)
print(tot)
# in one step:
res1=reduce(lambda a,b:a+b,filter(lambda y:y>=200,map(lambda y:y*0.9,products)))
print(res1)