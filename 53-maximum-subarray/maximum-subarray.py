class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n=len(nums)
        for i in range(1,n):
            nums[i]=max(nums[i],nums[i]+nums[i-1])
        return max(nums)