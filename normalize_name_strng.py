# Write a function normalize_name(s: str) -> str that:
# Strips extra whitespace,
# Converts to title case,
# Collapses multiple spaces into single spaces.
# If s is empty or contains only spaces, return "".

def normalize_name(s: str)->str:
    s1=""
    if s.isspace() or len(s)==0:
        return ""
    s=s.strip()
    s=s.title()
    word=s.split()
    s1+=" ".join(word)
    return s1

res=normalize_name("   loWer    Case ")
print(res)