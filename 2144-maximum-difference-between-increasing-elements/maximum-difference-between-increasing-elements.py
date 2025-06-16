class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        x=-1
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[j]>nums[i] and x<nums[j]-nums[i]:
                    x=nums[j]-nums[i]
        return x