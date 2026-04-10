class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        a=len(isConnected)
        visited=[False]*a
        x=0
        for i in range(a):
            if not visited[i]:
                x+=1
                b=[i]
                visited[i]=True
                while b:
                    c=len(b)
                    for _ in range(c):
                        d=b.pop(0)
                        for j in range(a):
                            if isConnected[d][j]==1 and not visited[j]:
                                visited[j]=True
                                b.append(j)
        return x