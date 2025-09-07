class Solution:
    def sumZero(self, n: int) -> List[int]:
        x=[]
        if n%2!=0:
            x.append(0)
        for i in range(1,n//2+1):
            x.append(-i)
            x.append(i)
        return x