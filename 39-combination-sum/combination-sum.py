class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        x=[]
        def helper(a,s,ind):
            if s==target:
                x.append(a[:])
                return
            if s>target:
                return
            for i in range(ind,len(candidates)):
                a.append(candidates[i])
                helper(a,s+candidates[i],i)
                a.pop()
        helper([], 0, 0)
        return x