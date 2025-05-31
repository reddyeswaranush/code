from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        assert n == len(board[0])
        n2 = n*n
        cells = []
        rev = False
        for idx in range(n - 1, -1, -1):
            cells.extend(reversed(board[idx]) if rev else board[idx])
            rev = not rev

        dist = [-1] * n2
        dist[0] = 0
        frontier = deque([1])
        while len(frontier):
            cur = frontier.popleft()
            d   = dist[cur - 1]
            assert d != -1
            if cur == n2:
                return d
            
            for nxt in range(cur + 1, min(cur + 6, n2) + 1):
                if cells[nxt - 1] != -1:
                    nxt = cells[nxt - 1]
                if dist[nxt - 1] == -1:
                    dist[nxt - 1] = d + 1
                    frontier.append(nxt)
        return -1