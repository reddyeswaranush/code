from collections import Counter
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        x=float("inf")
        a=Counter(list(word))
        for i in a:
            mi=0
            for j in a:
                if a[j]<a[i]:
                    mi+=a[j]
                elif a[j]>a[i]+k:
                    mi+=a[j]-a[i]-k
            if mi<x:
                x=mi
        return x