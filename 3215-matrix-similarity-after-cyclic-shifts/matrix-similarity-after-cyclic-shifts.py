class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        x = [row[:] for row in mat]
        m=len(mat)
        n=len(mat[0])
        k=k%n
        for _ in range(k):
            for i in range(m):
                a=mat[i]*2
                if i%2==0:
                    mat[i]=a[1:n+1]
                else:
                    mat[i]=a[n-1:2*n-1]
        if mat==x:
            return True
        else:
            return False