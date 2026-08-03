import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        dirr=[[1,0],[0,1],[-1,0],[0,-1]]
        n=len(heights)
        m=len(heights[0])
        dist=[[float('inf')]*m for _ in range(n)]
        dist[0][0]=0
        heap=[(0,0,0)]
        while heap:
            a=heapq.heappop(heap)
            if a[1]==n-1 and a[2]==m-1:
                return a[0]
            if a[0]>dist[a[1]][a[2]]:
                continue
            for i in dirr:
                x,y=a[1]+i[0],a[2]+i[1]
                if 0<=x<n and 0<=y<m:
                    new=max(a[0],abs(heights[x][y]-heights[a[1]][a[2]]))
                    if new<dist[x][y]:
                        dist[x][y]=new
                        heapq.heappush(heap,(new,x,y))
        return 0