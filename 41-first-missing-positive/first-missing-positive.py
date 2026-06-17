class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        a=set(nums)
        x=1
        while x in a:
            x+=1
        return x