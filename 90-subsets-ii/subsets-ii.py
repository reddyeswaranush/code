class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        x=set()
        n=len(nums)
        nums.sort()
        def helper(a,ind):
            if ind==n:
                x.add(tuple(a))
                return
            helper(a+[nums[ind]],ind+1)
            helper(a,ind+1)
        helper([],0)
        return [list(i) for i in x]