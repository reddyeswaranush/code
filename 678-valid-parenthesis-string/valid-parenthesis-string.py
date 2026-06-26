class Solution:
    def checkValidString(self, s: str) -> bool:
        open_par=[]
        star_par=[]
        n=len(s)
        for i in range(n):
            if s[i]=='(':
                open_par.append(i)
            elif s[i]=='*':
                star_par.append(i)
            else:
                if open_par:
                    open_par.pop()
                else:
                    if star_par:
                        star_par.pop()
                    else:
                        return False
        while open_par and star_par:
            if open_par[-1]<star_par[-1]:
                open_par.pop()
                star_par.pop()
            else:
                return False
        return len(open_par)==0