from math import gcd
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n=len(nums)
        x=0
        for i in range(n):
            p=1
            g=0
            l=1
            for j in range(i,n):
                p*=nums[j]
                g=gcd(g,nums[j])
                l=l*nums[j]//gcd(l,nums[j])
                if p==l*g:
                    x=max(x,j-i+1)
        return x