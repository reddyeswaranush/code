class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        a={}
        for i in range(len(groupSizes)):
            if groupSizes[i] not in a:
                a[groupSizes[i]]=[]
            a[groupSizes[i]].append(i)
        x=[]
        for i in a:
            j=0
            if len(a[i])<i:
                x.append(a[i])
            while j+i<=len(a[i]):
                x.append(a[i][j:j+i])
                j=j+i
        return x