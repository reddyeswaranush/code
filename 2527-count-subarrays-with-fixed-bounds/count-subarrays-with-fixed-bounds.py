class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        last_min = last_max = last_invalid = -1
        x = 0
        for i, j in enumerate(nums):
            if j < minK or j > maxK:
                 last_invalid = i
            if j == minK:          
                  last_min = i
            if j == maxK:  
                  last_max = i
            x += max(0, min(last_min, last_max) - last_invalid)
        return x