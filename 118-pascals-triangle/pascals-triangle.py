class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a=[[1],[1,1]]
        if numRows==1:
            return [[1]]
        elif numRows==2:
            return [[1],[1,1]]
        else:
            for _ in range(3,numRows+1):
                b=[]
                b.append(1)
                for i in range(1,len(a[-1])):
                    b.append(a[-1][i]+a[-1][i-1])
                b.append(1)
                a.append(b)
            return a