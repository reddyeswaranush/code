class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        x=0
        n=len(nums)
        for i in range(n-2):
            a=nums[i:i+3]
            if a[1]%2==0 and (a[0]+a[2])==a[1]//2:
                x+=1
        return x