class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        a=0
        ma=0
        j=0
        for i in range(n-1):
            ma=max(ma,i+nums[i])
            if a==i:
                j+=1
                a=ma
        return j