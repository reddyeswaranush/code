class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        x=[]
        for i in s:
            if not x or i=="(":
                x.append(i)
            else:
                if x[-1]=="(":
                    x.remove(x[-1])
                else:
                    x.append(i)
        return len(x)