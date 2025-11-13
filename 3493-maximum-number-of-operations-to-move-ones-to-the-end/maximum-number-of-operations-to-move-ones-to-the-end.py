class Solution:
    def maxOperations(self, s: str) -> int:
        x=0
        n=len(s)
        count=0
        i=0
        while i<n:
            if s[i]=='1':
                count+=1
                i+=1
            else:
                x+=count
                i+=1
                while i<n and s[i]=='0':
                    i+=1
        return x