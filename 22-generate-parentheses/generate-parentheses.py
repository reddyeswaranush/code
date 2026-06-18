class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        x=[]
        def helper(a,b,c):
            if len(a)==2*n:
                x.append(a)
                return
            if b<n:
                helper(a+'(',b+1,c)
            if c<b:
                helper(a+')',b,c+1)
        helper('',0,0)
        return x