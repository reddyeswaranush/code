class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        a=nums*2
        ans=[]
        n=len(nums)
        for i in range(n):
            b=a[i]
            found=False
            for j in range(i+1,2*n):
                if b<a[j]:
                    ans.append(a[j])
                    found=True
                    break
            if not found:
                ans.append(-1)
        return ans