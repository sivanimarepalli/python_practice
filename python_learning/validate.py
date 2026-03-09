username=input("Enter a user name: ")
if len(username)>12:
    print("Your username can't be morethan 12")
elif not username.find(" ")==-1:
    print("Username should not contain spaces")
elif not username.isdigit()==-1:
    print("Username should not contain digits")
else:
    print(f"Welcome {username}")