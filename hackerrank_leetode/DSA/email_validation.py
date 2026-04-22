# Email validation with enterprise rules using regular expression 
import re
email_val=list(input("Enter the email: ").split())
pattern=r'^[a-z0-9]+@gmail\.com$'
for e in email_val:
    res=re.match(pattern,e)
    if res:
        print("Valid")
    else:
        print("Invalid")