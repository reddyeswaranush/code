import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist=[float('inf')]*(n+1)
        dist[k]=0
        a={}
        b=[]
        for i in times:
            if i[0] not in a:
                a[i[0]]=[]
            a[i[0]].append([i[1],i[2]])
        heapq.heappush(b,(0,k))
        while b:
            dis,node=heapq.heappop(b)
            if dis>dist[node]:
                continue
            for i in a.get(node,[]):
                if dis+i[1]<dist[i[0]]:
                    dist[i[0]]=dis+i[1]
                    heapq.heappush(b,(dist[i[0]],i[0]))
        dist=dist[1:]
        return max(dist) if float('inf') not in dist else -1