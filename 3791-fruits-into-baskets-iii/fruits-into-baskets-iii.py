class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        size = 1
        while size<n: size*=2
        st = [0]*size*2
        for i, val in enumerate(baskets):
            st[i+size] = val
        for i in range(size-1, 0, -1):
            st[i] = max(st[i*2+1], st[i*2])
        
        x=0
        for f in fruits:
            cur = 1
            if f>st[cur]:
                x+=1
                continue
            while cur<size:
                if st[2*cur]>=f:
                    cur*=2
                else:
                    cur=cur*2+1
            st[cur] = 0
            cur//2
            while cur:
                cur = cur//2
                st[cur] = max(st[cur*2],st[cur*2+1])
        
        return x