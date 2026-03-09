# while loop:
name =input("Enter your name: ")
while name == "": # loops till user enters a name when prompted
    print("You did not enter your name")
    name =input("Enter your name: ")
print(f"Welcome {name}")