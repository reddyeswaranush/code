class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        y=0
        a=max(nums)
        x=[]
        for i in nums:
            if i==a:
                y=y+1
            else:
                x.append(y)
                y=0
        x.append(y)
        return max(x)