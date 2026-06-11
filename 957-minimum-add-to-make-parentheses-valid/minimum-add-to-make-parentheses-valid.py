class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        a=[]
        for i in s:
            if len(a)==0 or i=='(':
                a.append(i)
            else:
                if a[-1]=='(':
                    a.pop()
                else:
                    a.append(i)
        return len(a)