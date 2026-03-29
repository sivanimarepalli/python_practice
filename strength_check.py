# Create check_strength(pwd: str, min_len=8) -> dict returning:
# {
#   "length_ok": bool,
#   "has_upper": bool,
#   "has_lower": bool,
#   "has_digit": bool,
#   "has_special": bool,
#   "score": int  # sum of True values
# }
# Special characters are anything not alphanumeric.
def check_strength(pwd:str,min_len=8)->dict:
    res={"length_ok":False,"has_upper":False,"has_lower":False,"has_digit":False,"has_special":False}
    s=0
    if len(pwd)>=min_len:
        res["length_ok"]=True
    for ch in pwd:
        if ch.isupper():
            res["has_upper"]=True
        elif ch.islower():
            res["has_lower"]=True
        elif ch.isnumeric():
            res["has_digit"]=True
        elif not ch.isalnum():
            res["has_special"]=True
    for v in res.values():
        if v:
            s+=1
    res["score"]=s
    return res

c=check_strength("Apple")
print(c)

