class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n=len(nums)
        a=[0]*(n+1)
        for i in queries:
            a[i[0]]-=1
            a[i[1]+1]+=1
        curr=0
        for i in range(n):
            curr+=a[i]
            if nums[i]+curr>0:
                return False
        return True