class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        dp = [[dict() for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row == 0 and col == 0:
                    dp[row][col][grid[row][col] % k] = 1
                    continue
                if row > 0:
                    for rem,count in dp[row-1][col].items():
                        rem = (rem + grid[row][col] % k) % k
                        if rem in dp[row][col]:
                            dp[row][col][rem] = (dp[row][col][rem] + count) % 1000000007
                        else:    
                            dp[row][col][rem] = count % 1000000007
                if col > 0:
                    for rem,count in dp[row][col-1].items():
                        rem = (rem + grid[row][col] % k) % k
                        if rem in dp[row][col]:
                            dp[row][col][rem] = (dp[row][col][rem] + count) % 1000000007
                        else:    
                            dp[row][col][rem] = count % 1000000007
        if 0 not in  dp[len(dp)-1][len(dp[0])-1]:
            return 0
        return dp[len(dp)-1][len(dp[0])-1][0]