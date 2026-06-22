class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        a=[1]*n
        for i in range(1,n):
            if ratings[i-1]<ratings[i]:
                a[i]=a[i-1]+1
        for i in range(n-2,-1,-1):
            if ratings[i+1]<ratings[i]:
                a[i]=max(a[i+1]+1,a[i])
        print(a)
        return sum(a)