class Solution:
    def canPartitionGrid(self, grid):
        m, n = len(grid), len(grid[0])
        
        total = sum(sum(row) for row in grid)

        curr = 0
        for i in range(m):
            curr += sum(grid[i])
            if curr * 2 == total:
                return True
        
        curr = 0
        for j in range(n):
            col_sum = 0
            for i in range(m):
                col_sum += grid[i][j]
            curr += col_sum
            if curr * 2 == total:
                return True
        
        return False