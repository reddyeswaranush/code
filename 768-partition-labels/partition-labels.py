class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        a=list(set(list(s)))
        b=[]
        for i in a:
            b.append([s.index(i),s.rindex(i)])
        b.sort()
        y=[]
        for i in b:
            if not y or y[-1][1]<i[0]:
                y.append(i)
            else:
                y[-1][1]=max(y[-1][1],i[1])
        x=[]
        for i in y:
            x.append(i[1]-i[0]+1)
        return x