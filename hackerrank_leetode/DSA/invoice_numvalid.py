# Invoice number validation with checksum stub - Invoices follow INV-<year><month>-<serial> e.g., INV-202511-000123; year is 4 digits, month 01–12, serial exactly 6 digits.
import re
text=input("Enter a text: ")
pattern=r'INV-\d{4}(0[1-9]|1[0-2])-\d{6}'
res=re.fullmatch(pattern,text)
if res:
    print("valid")
else:
    print("Invalid")