import math
class Solution:
    def countTriples(self, n: int) -> int:
        x=0
        for i in range(1,n+1):
            for j in range(1,n+1):
                a=math.sqrt(i**2+j**2)
                if a<=n and a%1==0:
                    x+=1
        return x