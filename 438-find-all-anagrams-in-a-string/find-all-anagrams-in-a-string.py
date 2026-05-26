from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        a=len(p)
        b=Counter(p)
        c=Counter(s[:a])
        x=[]
        if b==c:
            x.append(0)
        for i in range(a,len(s)):
            if s[i] not in c:
                c[s[i]]=0
            c[s[i]]+=1 
            c[s[i-a]]-=1
            if c[s[i-a]]==0:
                del c[s[i-a]]
            if c==b:
                x.append(i-a+1)
        return x