class Solution:
    def numSub(self, s: str) -> int:
        x=0
        ans=0
        for i in s:
            if i=='1':
                x+=1
            else:
                ans+=(x+1)*x//2
                x=0
        ans+=(x+1)*x//2
        return ans%((10**9)+7)