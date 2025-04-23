class Solution:
    def countLargestGroup(self, n: int) -> int:
        y={}
        x=0
        max_size=-1
        for i in range(1,n+1):
            a=sum(map(int,str(i).strip()))
            if a not in y:
                y[a]=0
            y[a]+=1
            if y[a]>max_size:
                max_size=y[a]
        for i in y:
            if y[i]==max_size:
                x+=1
        return x