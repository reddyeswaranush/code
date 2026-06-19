class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x={}
        for i in nums:
            if i not in x:
                x[i]=0
            x[i]=x[i]+1
        a=len(nums)/2
        for i in x.keys():
            if x[i]>a:
                return i