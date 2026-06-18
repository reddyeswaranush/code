class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        x=[]
        n=len(candidates)
        candidates.sort()
        def helper(a,s,ind):
            if s==target and a not in x:
                x.append(a[:])
                return 
            if s>target:
                return
            for i in range(ind,n):
                if i>ind and candidates[i]==candidates[i-1]:
                    continue
                else:
                    a.append(candidates[i])
                    helper(a,s+candidates[i],i+1)
                    a.pop()
        helper([],0,0)
        return x