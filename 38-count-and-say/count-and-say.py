class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        b=self.countAndSay(n-1)
        x=""
        count=1
        for i in range(1,len(b)):
            if b[i]==b[i-1]:
                count+=1
            else:
                x+=str(count)+b[i-1]
                count=1
        x+=str(count)+b[-1]
        return x