class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        a=1<<n
        x=[]
        for i in range(a):
            b=[]
            for j in range(n):
                if i&(1<<j):
                    b.append(nums[j])
            x.append(b)
        return x