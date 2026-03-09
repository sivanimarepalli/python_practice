import random
#print(help(random)) # provides entire retails about the random module
number=random.randint(1,6) # it will generate a random integer value in the range 1 to 6
print(number)
# to generate a random floating point number  between 0 and 1
no=random.random()
print(no)
options=("rock","paper","scissors")
# choice() is mainly ised for games if you ever need a random element
option=random.choice(options) # it will randomly return an choice from the tuple we create
print(option)
# shuffle()-> we can shuffle the sequence that we previously provided
cards=["2","3","4","5","6","7","8","9","10","J","K","Q","A"]
random.shuffle(cards)
print(cards)