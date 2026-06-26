class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        x=0
        c=0
        n=len(nums)
        for i in range(n):
            if nums[i]==0:
                c+=1
            if c>k:
                if nums[left]==0:
                    c-=1
                left+=1
            x=max(x,i-left+1)
        return x