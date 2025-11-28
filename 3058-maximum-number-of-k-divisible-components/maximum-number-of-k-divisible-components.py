class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = [set() for _ in range(n)]
        degree = [0] * n
        for a,b in edges:
            graph[a].add(b)
            graph[b].add(a)
            degree[a] += 1
            degree[b] += 1

        x = 0       

        q = deque([i for i,d in enumerate(degree) if d == 1])
        while q:
            i = q.pop()
            
            if values[i] % k == 0:
                x += 1

            if graph[i]: 
                j = graph[i].pop()
                graph[j].remove(i)
                degree[j] -= 1
                if degree[j] == 1:
                    q.append(j)
                values[j] = (values[j] + values[i]) % k            

        return x or 1