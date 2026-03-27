#Question: Given a string containing letters, digits, and symbols, determine if it reads the same forwards and backwards when considering only alphabetic characters (case-insensitive).
# timecomplexity is o(N).
def isAlphabeticPalindrome(code):
    # Write your code here
    res=""
    for ch in code:
        if ch.isalpha():
            res="".join(ch)
    res=res.lower()
    rev_res=res[::-1]
    if res == rev_res:
        return True
    else:
        return False
        
code = input()

result = isAlphabeticPalindrome(code)

print(int(result))
