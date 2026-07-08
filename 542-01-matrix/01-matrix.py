from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        q=deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    q.append((i,j))
                else:
                    mat[i][j]=-1
        while q:
            x,y=q.popleft()
            for i,j in [[-1,0],[0,-1],[1,0],[0,1]]:
                mx,my=x+i,y+j
                if 0<=mx<m and 0<=my<n and mat[mx][my]==-1:
                    mat[mx][my]=mat[x][y]+1
                    q.append((mx,my))
        return mat