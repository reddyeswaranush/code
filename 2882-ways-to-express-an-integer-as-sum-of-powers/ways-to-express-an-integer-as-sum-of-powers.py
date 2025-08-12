class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7

        def backtrack(n, pos, memo={}):
            if n == 0:
                return 1
            if n < 0 or pow(pos, x) > n:
                return 0
            
            if (n, pos) in memo:
                return memo[(n, pos)]
            
            pick = backtrack(n - pow(pos, x), pos + 1)
            skip = backtrack(n, pos + 1)

            memo[(n, pos)] = (pick + skip) % MOD
            return memo[(n, pos)]
        
        return backtrack(n, 1)