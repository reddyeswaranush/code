from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        a=Counter(s1)
        b=Counter(s2[:k])
        if a==b:
            return True
        for i in range(k,len(s2)):
            b[s2[i]]+=1
            b[s2[i-k]]-=1
            if b[s2[i-k]]==0:
                del b[s2[i-k]]
            if a==b:
                return True
        return False