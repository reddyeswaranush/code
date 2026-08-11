class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp={}
        n=len(grid)
        m=len(grid[0])
        def search(i,j):
            if i==n-1 and j==m-1:
                return grid[i][j]
            if i>=n or j>=m:
                return float('inf')
            if (i,j) in dp:
                return dp[(i,j)]
            dp[(i,j)]=grid[i][j]+min(search(i+1,j),search(i,j+1))
            return dp[(i,j)]
        return search(0,0)