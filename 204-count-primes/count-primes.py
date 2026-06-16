class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        a=[True]*n
        a[0]=False
        a[1]=False
        for i in range(2,int(n**0.5)+1):
            if a[i]:
                for j in range(i*i,n,i):
                    a[j]=False
        b=0
        for i in a:
            if i:
                b+=1
        return b