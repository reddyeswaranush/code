class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        x=set()
        n=len(nums)
        for i in range(n):
            left=i+1
            right=n-1
            while left<right:
                a=nums[i]+nums[left]+nums[right]
                if a==0:
                    x.add((nums[i],nums[left],nums[right]))
                    left+=1
                    right-=1
                elif a>0:
                    right-=1
                else:
                    left+=1
        return list(x)