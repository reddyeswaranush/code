class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        def search(i,j):
            if 0<=i<m and 0<=j<n and grid[i][j]=='1':
                grid[i][j]='2'
                search(i+1,j)
                search(i,j+1)
                search(i-1,j)
                search(i,j-1)
            return 
        x=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    x+=1
                    search(i,j)
        return x