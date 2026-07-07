from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        q=deque()
        f=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    f+=1
        time=0
        dirr=[[0,1],[1,0],[0,-1],[-1,0]]
        while q and f>0:
            a=len(q)
            time+=1
            for _ in range(a):
                b=q.popleft()
                for i in dirr:
                    x=b[0]+i[0]
                    y=b[1]+i[1]
                    if 0<=x<m and 0<=y<n and grid[x][y]==1:
                        f-=1
                        grid[x][y]=2
                        q.append((x,y))

        return time if f==0 else -1