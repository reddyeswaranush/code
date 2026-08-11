class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp={}
        def search(i,j):
            if i==m-1 and j==n-1:
                return 1
            if i>=m or j>=n:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            dp[(i,j)]=search(i+1,j)+search(i,j+1)
            return dp[(i,j)]
        return search(0,0)