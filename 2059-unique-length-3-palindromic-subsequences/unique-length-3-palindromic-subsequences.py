class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        x = 0
        for c in set(s):
            i, j = s.find(c), s.rfind(c)
            if j > i + 1:
                x += len(set(s[i+1:j]))
        return x