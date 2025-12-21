class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        x={}
        n=len(s)
        for i in range(n):
            if s[i] not in x:
                x[s[i]]=[]
            x[s[i]].append(i)
        for i in range(n):
            x[t[i]].append(i)
        ans=0
        for i in x.keys():
            ans+=abs(x[i][0]-x[i][1])
        return ans