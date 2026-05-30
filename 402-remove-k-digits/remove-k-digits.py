class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n=len(num)
        if n<=k:
            return "0"
        x=[int(num[0])]
        a=0
        for i in num[1:]:
            while x and a<k and int(i)<x[-1]:
                x.pop()
                a+=1
            x.append(int(i))
        while a<k:
            x.pop()
            a+=1
        ans=''
        for i in x:
            ans+=str(i)
        ans=ans.lstrip('0')
        if ans=='':
            return "0"
        return ans