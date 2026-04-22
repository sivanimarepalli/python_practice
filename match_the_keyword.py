# Detect Presence of a Keyword  in a sentence.
import re
text=list(input("Enter the text: ").split())
keywords=['python','java','c++','c','AND','OR','NOT']
m=[]
for wrd in text:
    for w in keywords:
        pattern=r'\b'+ re.escape(w)+r'\b'
        if re.search(pattern,wrd,flags=re.IGNORECASE):
            m.append(wrd)
            break
for ele in m:
    print(ele)
