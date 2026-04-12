from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = -1
        while q:
            i, j = q.popleft()
            for x, y in [(1,0), (-1,0), (0,1), (0,-1)]:
                n1, n2 = i + x, j + y
                if 0 <= n1 < m and 0 <= n2 < n and mat[n1][n2] == -1:
                    mat[n1][n2] = mat[i][j] + 1
                    q.append((n1, n2))
        return mat