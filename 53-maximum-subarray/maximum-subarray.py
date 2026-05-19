class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        a=[0]*n
        for i in range(n):
            if a[i-1]<0:
                b=nums[i]
            else:
                b=a[i-1]+nums[i]
            a[i]=b
        return max(a)