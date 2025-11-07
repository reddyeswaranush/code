class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[-1]*n
        stack=[]
        for i in range(2*n):
            b=nums[i%n]
            while stack and nums[stack[-1]]<b:
                ans[stack[-1]]=b
                stack.pop()
            if i<n:
                stack.append(i)
        return ans