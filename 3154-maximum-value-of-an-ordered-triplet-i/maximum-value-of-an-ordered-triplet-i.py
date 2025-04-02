class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        x=0
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if (nums[i]-nums[j])*nums[k]>x:
                        x=(nums[i]-nums[j])*nums[k]
        return x