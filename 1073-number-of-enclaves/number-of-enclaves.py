class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        def search(i,j):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j]!=1:
                return 
            grid[i][j]='S'
            search(i-1,j)
            search(i+1,j)
            search(i,j-1)
            search(i,j+1)
            return 
        for i in range(m):
            if grid[i][0]==1:
                search(i,0)
            if grid[i][n-1]==1:
                search(i,n-1)
        for j in range(n):
            if grid[0][j]==1:
                search(0,j)
            if grid[m-1][j]==1:
                search(m-1,j)
        x=0
        for i in range(m):
            print(grid[i])
            for j in range(n):
                if grid[i][j]==1:
                    x+=1
        return x