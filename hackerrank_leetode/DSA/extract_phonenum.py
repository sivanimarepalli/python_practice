# Natural text: extract phone numbers in multiple formats
import re
text=input("Enter your text: ")
pattern= r'\d{10}|\+\d{2}-\d{5}-\d{5}|\(\d{3}\)\s\d{8}'
res=re.findall(pattern,text)
for e in res:
    print(e)