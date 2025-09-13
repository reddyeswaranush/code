from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        a=['a','e','i','o','u']
        b=Counter(list(s))
        max_vo=0
        max_nvo=0
        for i in b:
            if i in a:
                max_vo=max(max_vo,b[i])
            else:
                max_nvo=max(max_nvo,b[i])
        return max_vo+max_nvo