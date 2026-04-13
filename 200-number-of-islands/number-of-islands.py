class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m=len(grid)
        n=len(grid[0])
        def search(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]!='1':
                return
            if grid[i][j]=='1':
                grid[i][j]=2
                search(i-1,j)
                search(i+1,j)
                search(i,j-1)
                search(i,j+1)
        x=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    search(i,j)
                    x+=1
        return x