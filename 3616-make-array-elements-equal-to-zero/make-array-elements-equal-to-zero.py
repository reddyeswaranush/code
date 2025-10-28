class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        def ans(a,i,d):
            n=len(a)
            curr=i
            while 0<=curr<n:
                if a[curr]==0:
                    curr+=d
                else:
                    a[curr]-=1
                    d=-d
                    curr+=d
            return a==[0]*n
        x=0
        for i in range(len(nums)):
            if nums[i]!=0:
                continue
            if ans(nums[:],i,1):
                x+=1
            if ans(nums[:],i,-1):
                x+=1
        return x