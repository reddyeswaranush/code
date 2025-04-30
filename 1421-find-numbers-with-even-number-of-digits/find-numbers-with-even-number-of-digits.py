class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        x=0
        for i in nums:
            if len(str(i))%2==0:
                x+=1
        return x