# You’re given a list of product names with inconsistent casing and extra spaces: 
# names = ["  alpha Case  ", "Beta   unit", "gAmMa MODULE  "]
# Use map with a lambda to strip spaces and convert to Title Case (e.g., "Alpha Case").
names = ["  alpha Case  ", "Beta   unit", "gAmMa MODULE  "]
def strip_space(names):
    name=list(map(lambda x:x.strip().title(),names))
    print(name)

strip_space(names)