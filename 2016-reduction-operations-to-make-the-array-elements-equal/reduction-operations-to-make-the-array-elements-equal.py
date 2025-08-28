from collections import Counter
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        a=Counter(nums)
        if len(a)==1:
            return 0
        else:
            b=sorted(list(a.keys()))
            x=0
            for i in range(len(b)-1,0,-1):
                x+=a[b[i]]
                a[b[i-1]]=a[b[i]]+a[b[i-1]]
            return x