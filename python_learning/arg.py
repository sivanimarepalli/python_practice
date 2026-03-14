def net_price(list_price,discount,tax):
    return list_price*(1-discount)*(1+tax)

print("Positional arguments value: ",net_price(500,0,0.05)) # positional as the values passed should match the parameters provided in the function name

#type-2
# default arguments= can assign the values when we pass the arguments

def nett_price(listt_price,discountt=0,taxx=0.05):
    return listt_price*(1-discountt)*(1+taxx)

print("default arguments value: ",nett_price(555)) # we can pass a new value to the default arguments then new value-> overrides old value
