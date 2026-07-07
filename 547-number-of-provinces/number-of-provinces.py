class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        visited=[False]*n
        m={}
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1:
                    if i not in m:
                        m[i]=[]
                    m[i].append(j)
        print(m)
        def dfs(a):
            if not visited[a]:
                visited[a]=True
                for i in m[a]:
                    if not visited[i]:
                        dfs(i)
        x=0
        for i in range(n):
            if not visited[i]:
                x+=1
                dfs(i)
        return x