class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        x=0
        l=0
        for i in dimensions:
            if i[0]**2+i[1]**2>l:
                x=i[0]*i[1]
                l=i[0]**2+i[1]**2
            elif i[0]**2+i[1]**2==l:
                x=max(i[0]*i[1],x)
        return x