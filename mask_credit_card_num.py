# Replace all digits in a credit card number except the last 4 with *.
import re
credit_num=input("Enter the credit card number: ")
n=len(credit_num)-4
pattern=""
for _ in range(n):
    pattern+='*'
pattern+=credit_num[n:]
print(pattern)
# another way
result = re.sub(r'\d(?=\d{4})', '*', credit_num)
print(result)