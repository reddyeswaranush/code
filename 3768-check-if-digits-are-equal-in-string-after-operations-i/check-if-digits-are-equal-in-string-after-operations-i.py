class Solution:
    def hasSameDigits(self, s: str) -> bool:
        def ans(a):
            b=''
            for i in range(len(a)-1):
                b=b+str((int(s[i])+int(s[i+1]))%10)
            return b

        while len(s)!=2:
            x=ans(s)
            print(x)
            s=x
        return s[0]==s[1]