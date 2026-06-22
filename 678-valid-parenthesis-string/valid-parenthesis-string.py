class Solution:
    def checkValidString(self, s: str) -> bool:
        a=[]
        b=[]
        for i in range(len(s)):
            if s[i]=='(':
                a.append(i)
            elif s[i]=='*':
                b.append(i)
            else:
                if a:
                    a.pop()
                elif b:
                    b.pop()
                else:
                    return False
        while a and b:
            if a[-1]<b[-1]:
                a.pop()
                b.pop()
            else:
                return False
        return len(a)==0