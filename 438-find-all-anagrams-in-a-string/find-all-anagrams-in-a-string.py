from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        a=len(p)
        b=Counter(p)
        x=[]
        for i in range(len(s)-a+1):
            if Counter(s[i:i+a])==b:
                x.append(i)
        return x