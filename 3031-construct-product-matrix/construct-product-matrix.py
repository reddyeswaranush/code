class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        m=len(grid[0])
        MOD=12345
        prefix=[[1]*m for _ in range(n)]
        sufix=[[1]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if j>0:
                    prefix[i][j]=(grid[i][j-1]%MOD*prefix[i][j-1]%MOD)%MOD
                elif i>0:
                    prefix[i][j]=(grid[i-1][m-1]%MOD*prefix[i-1][m-1]%MOD)%MOD
        
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if j<m-1:
                    sufix[i][j]=(grid[i][j+1]%MOD*sufix[i][j+1]%MOD)%MOD
                elif i<n-1:
                    sufix[i][j]=(grid[i+1][0]%MOD*sufix[i+1][0]%MOD)%MOD
        
        for i in range(n):
            for j in range(m):
                prefix[i][j]=(prefix[i][j]*sufix[i][j])%MOD
        return prefix