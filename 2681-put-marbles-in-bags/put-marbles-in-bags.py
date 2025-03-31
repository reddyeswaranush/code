class Solution:
    def putMarbles(self, weight: List[int], k: int) -> int:
        if k==1 or k==len(weight): return 0
        a = []
        for i in range(len(weight)-1):
            a.append(weight[i]+weight[i+1])
        a.sort()
        return sum(a[-(k-1):])-sum(a[:k-1])