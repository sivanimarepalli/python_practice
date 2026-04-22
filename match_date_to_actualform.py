# Given strings like "2025-11-30 Report Generated", use match() to confirm if the string starts with a date in YYYY-MM-DD format.
import re
date=input("Enter the date: ")
pattern=r'\d{4}-\d{2}-\d{2}'
res=re.match(pattern,date,flags=0)
if res:
    print("Valid")
else:
    print("Invalid")