class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        x=0
        n=len(nums)
        for i in range(n-1):
            if abs(sum(nums[:i])-sum(nums[i:]))%2==0:
                x+=1
        return x