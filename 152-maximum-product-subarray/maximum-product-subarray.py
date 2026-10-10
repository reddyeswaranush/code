class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        maxx=nums[0]
        minn=nums[0]
        a=nums[0]
        for i in nums[1:]:
            temp=maxx
            maxx=max(i,maxx*i,minn*i)
            minn=min(i,temp*i,minn*i)
            a=max(a,maxx)
        return a