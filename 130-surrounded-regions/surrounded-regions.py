class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m=len(board)
        n=len(board[0])
        def help(i,j):
            if 0<=i<m and 0<=j<n and board[i][j]=='O':
                board[i][j]='S'
                help(i+1,j)
                help(i,j+1)
                help(i-1,j)
                help(i,j-1)
            return 
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O' and i in [0,m-1] or j in [0,n-1]:
                    help(i,j)
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='S':
                    board[i][j]='O'