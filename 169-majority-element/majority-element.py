class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a=0
        b=0
        for i in nums:
            if b==0:
                a=i
            if i==a:
                b+=1
            else:
                b-=1
        return a