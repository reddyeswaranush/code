from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        q=deque()
        fresh=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        
        ans=0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while q and fresh>0:
            for _ in range(len(q)):
                x,y=q.popleft()
                for i,j in directions:
                    nx,ny=x+i,y+j
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        q.append((nx, ny))
            
            ans += 1
        
        return ans if fresh == 0 else -1