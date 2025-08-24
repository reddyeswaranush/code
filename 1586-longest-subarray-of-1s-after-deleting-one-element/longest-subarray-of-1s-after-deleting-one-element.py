class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        a=0
        x=[]
        n=len(nums)
        for i in range(n):
            if nums[i]==1:
                a+=1
            else:
                x.append(a)
                a=0
        x.append(a)
        if len(x)==1:
            return x[0]-1
        else:
            y=0
            for i in range(len(x)-1):
                y=max(y,x[i]+x[i+1])
            return y