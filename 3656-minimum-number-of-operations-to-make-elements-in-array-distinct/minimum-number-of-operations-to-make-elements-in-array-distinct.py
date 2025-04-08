class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        x=0
        if len(nums)<=3 and len(set(nums))==len(nums):
            return 0
        elif len(nums)<=3 and len(set(nums))!=len(nums):
            return 1
        while len(set(nums))!=len(nums):
            x+=1
            if len(nums)<3:
                return x
            nums=nums[3:]
        return x