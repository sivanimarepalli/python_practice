# keyword arguments

def hello(greeting,title,first,last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", " Ms.",first="Sivani",last="Marepalli") # in keyword arguments use var names while calling like here i.e first="sivani"
 
 # Note: positional arguments should always be placed at first

 # end is a keyword that can be used in print()
 # sep is a keyword that can be used in print()

 # ex-2:
def get_phone(country,area,firstt,lastt):
    return f"{country}-{area}-{firstt}-{lastt}"

print(get_phone(country=91,area=123,firstt=567,lastt=985))