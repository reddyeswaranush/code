class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        x=abs(nums[0]-nums[-1])
        n=len(nums)
        for i in range(n-1):
            if abs(nums[i+1]-nums[i])>x:
                x=abs(nums[i+1]-nums[i])
        return x