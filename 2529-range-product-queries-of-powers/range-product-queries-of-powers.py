import math
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def closest_power_of_two(t):
            if n < 1:
                return None
            return 2 ** math.floor(math.log2(n))
        m=10**9+7
        a=[]
        while n>0:
            b=closest_power_of_two(n)
            a.append(b)
            n=n-b
        a=a[::-1]
        x=[]
        for i in queries:
            x.append(math.prod(a[i[0]:i[1]+1])%m)
        return x