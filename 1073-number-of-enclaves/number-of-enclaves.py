class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        def help(i,j):
            if 0<=i<m and 0<=j<n and grid[i][j]==1:
                grid[i][j]=-1
                help(i+1,j)
                help(i-1,j)
                help(i,j+1)
                help(i,j-1)
            return 
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and i in [0,m-1] or j in [0,n-1]:
                    help(i,j)
        x=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    x+=1
        return x