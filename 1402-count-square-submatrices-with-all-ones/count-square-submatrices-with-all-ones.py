class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row=len(matrix)
        col=len(matrix[0])
        x=0
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==1:
                    if i>0 and j>0:
                        matrix[i][j]=min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])+1
                    x+=matrix[i][j]
        return x