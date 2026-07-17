class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        ma=0
        for i in range(n):
            if ma<i:
                return False
            ma=max(ma,i+nums[i])
        return True