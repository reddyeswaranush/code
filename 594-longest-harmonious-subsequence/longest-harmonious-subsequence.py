class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        x = 0 
        for j in range(len(nums)):
            while nums[j] - nums[i] > 1:
                i += 1

            if nums[j] - nums[i] == 1:
                x = max(x, j - i + 1)
        
        return x