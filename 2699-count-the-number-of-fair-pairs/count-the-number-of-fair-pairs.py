from bisect import bisect_left, bisect_right
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        x=0
        nums.sort()
        n=len(nums)
        for i in range(n):
            a=bisect_left(nums,lower-nums[i],i+1,n)
            b=bisect_right(nums,upper-nums[i],i+1,n)
            x+=(b-a)
        return x