class Solution:
    def longestPrefix(self, s: str) -> str:
        x=""
        for i in range(len(s)):
            if s.startswith(s[:i]) and s.endswith(s[:i]):
                if len(s[:i])>len(x):
                    x=s[:i]
        return x