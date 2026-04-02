# Given a string s consisting of words and spaces, return the length of the last word in the string. A word is a maximal substring consisting of non-space characters only.
# simple way using split():
def lengthOfLastWord(s: str) -> int:
        ele= s.split()
        return len(ele[-1])
# approach 2 without using split():
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        cnt=0
        for ch in s[::-1]:
            if ch!=" ":
                cnt+=1
            elif ch==" ":
                break
        return cnt
        
