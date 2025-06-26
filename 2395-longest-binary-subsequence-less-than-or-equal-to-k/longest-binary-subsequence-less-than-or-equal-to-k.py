class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        dp = [k+1] * (n + 1)
        dp[0] = 0
    
        for ch in s:
            bit = 1 if ch == '1' else 0
            for j in range(n - 1, -1, -1):
                val = dp[j]
                if val <= k:
                    new = (val << 1) | bit  #val * 2 + bit
                    if new > k:
                        new = k + 1
                    if new < dp[j + 1]:
                        dp[j + 1] = new
        for j in range(n, -1, -1):
            if dp[j] <= k:
                return j
        return 0