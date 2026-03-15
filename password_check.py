# Password Check with Limited Attempts
actual_password="Apple"
limit=3
flag=False
while limit>0:
    password=input("Enter the password: ").title()
    if password==actual_password:
        flag=True
        break
    elif password!=actual_password:
        limit-=1
    else:
        flag=False
if flag:
    print("Access Granted")
else:
     print("Account Locked")