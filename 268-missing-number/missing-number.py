class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a=sum(nums)
        b=max(nums)
        c=(b*(b+1)/2)
        if c==a and 0 in nums:
            return b+1
        elif c==a and 0 not in nums:
            return 0
        else:
            return int(c-a)