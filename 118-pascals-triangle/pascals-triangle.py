class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        elif numRows==2:
            return [[1],[1,1]]
        else:
            x=[]
            t=[1,1]
            a=[]
            x.append([1])
            x.append([1,1])
            for i in range(numRows-2):
                for i in range(len(t)-1):
                    a.append(t[i]+t[i+1])
                x.append([1]+a+[1])
                t=[1]+a+[1]
                a=[]
            return x