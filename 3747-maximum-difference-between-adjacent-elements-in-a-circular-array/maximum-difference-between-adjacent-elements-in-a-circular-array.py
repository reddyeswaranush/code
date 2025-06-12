class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        x=[]
        n=len(nums)
        for i in range(n-1):
            x.append(abs(nums[i+1]-nums[i]))
        x.append(abs(nums[0]-nums[-1]))
        return max(x)