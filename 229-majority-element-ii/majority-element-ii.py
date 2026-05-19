class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        a={}
        for i in nums:
            if i not in a:
                a[i]=0
            a[i]+=1
        x=[]
        for i in a:
            if a[i]>n/3:
                x.append(i)
        return x