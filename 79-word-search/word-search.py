class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n=len(board)
        m=len(board[0])
        o=len(word)
        a=set()
        def helper(s,ind1,ind2,ind):
            if ind==o:
                return True
            if ind1<0 or ind2<0 or ind1>=n or ind2>=m or (ind1,ind2) in a:
                return False
            if board[ind1][ind2]!=word[ind]:
                return False
            a.add((ind1,ind2))
            x=helper(s+word[ind],ind1+1,ind2,ind+1) or helper(s+word[ind],ind1-1,ind2,ind+1) or helper(s+word[ind],ind1,ind2+1,ind+1) or helper(s+word[ind],ind1,ind2-1,ind+1)
            a.remove((ind1,ind2))
            return x
        for i in range(n):
            for j in range(m):
                if helper('',i,j,0):
                    return True
        return False