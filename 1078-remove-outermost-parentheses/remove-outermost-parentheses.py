class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        a = 0
        x = ""
        for i in s:
            if i=='(':
                if a>0:
                    x+=i
                a+=1
            else:
                a-=1
                if a>0:
                    x+=i
        return x