import bisect
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        x=0
        n=len(nums)
        nums.sort()
        for i in range(n):
            for j in range(i+1,n):
                tar=nums[i]+nums[j]
                k = bisect.bisect_left(nums, tar, j+1)
                x+=(k-(j+1))
        return x