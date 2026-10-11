class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if nums==[]:
            return 0
        nums=list(set(nums))
        nums.sort()
        a=1
        x=1
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:
                a+=1
                x=max(x,a)
            else:
                a=1
        return x