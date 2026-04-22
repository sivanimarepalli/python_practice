# Extract Domain Names from Emails
import re
text=list(input("Enter a mail: ").split())
for wrd in text:
    pattern=re.findall(r'(?<=@).*',wrd)
    for w in pattern:
        print(w)


