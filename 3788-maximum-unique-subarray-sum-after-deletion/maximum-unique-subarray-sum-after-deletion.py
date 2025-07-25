from collections import Counter
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        a=Counter(nums)
        y=0
        x=float('-inf')
        for i in a:
            if i>=0:
                y+=i
        x=max(x,y)
        if x==0:
            return max(nums)
        return x