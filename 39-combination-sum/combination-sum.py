class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        x=[]
        index=0
        n=len(candidates)
        def ans(index,total,a):
            if index==n or total>target:
                return
            if total==target:
                x.append(a.copy())
                return 
            a.append(candidates[index])
            ans(index,total+candidates[index],a)
            a.pop()
            ans(index+1,total,a)
        ans(0,0,[])
        return x     