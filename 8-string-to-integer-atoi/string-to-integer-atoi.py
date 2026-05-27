class Solution:
    def myAtoi(self, s: str) -> int:
        x=''
        sign=1
        i=0
        n=len(s)
        while i<n and s[i]==' ':
            i+=1
        if i<n and (s[i]=='-' or s[i]=='+'):
            if s[i]=='-':
                sign=-1
            i+=1
        while i<n and s[i].isdigit():
            x+=s[i]
            i+=1
        if x=='':
            return 0
        x=sign*int(x)
        if x<-2147483648:
            return -2147483648
        if x>2147483647:
            return 2147483647
        return x