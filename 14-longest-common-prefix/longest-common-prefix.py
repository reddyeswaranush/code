class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x=min(sorted(strs,key=len))
        for i in range(len(x),-1,-1):
            if all(j.startswith(x[:i]) for j in strs):
                return x[:i]
        return ""