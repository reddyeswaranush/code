class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[-1]
        a=[0]*(n)
        a[0]=nums[0]
        for i in range(1,n):
            a[i]=max(a[i-1]+nums[i],nums[i])
        return max(a)