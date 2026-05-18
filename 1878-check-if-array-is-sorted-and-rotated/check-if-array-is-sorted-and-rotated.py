class Solution:
    def check(self, nums: List[int]) -> bool:
        if nums.count(nums[0])==len(nums):
            return True
        nums=nums+nums
        x=1
        n=len(nums)
        ans=0
        for i in range(1,n):
            if nums[i]>=nums[i-1]:
                x+=1
                ans=max(ans,x)
            else:
                x=1
        ans=max(ans,x)
        if ans==n//2:
            return True
        else:
            return False