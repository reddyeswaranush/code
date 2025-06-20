class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        x=0
        n=len(nums)
        for i in range(n):
            for j in range(n):
                if nums[i]+nums[j]==target and i!=j:
                    x+=1
        return x