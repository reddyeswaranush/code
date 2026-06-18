class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        x=set()
        def helper(a,ind):
            if len(a)==k and sum(a)==n:
                x.add(tuple(a))
                return
            if ind==10:
                return
            helper(a+[ind],ind+1)
            helper(a,ind+1)
        helper([],1)
        return [list(i) for i in x]