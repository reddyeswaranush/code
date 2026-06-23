class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x:(x[0],x[1]))
        x=[]
        for i in intervals:
            if not x: 
                x.append(i)
            elif x[-1][1]<i[0]:
                x.append(i)
            else:
                x[-1][1]=max(x[-1][1],i[1])
        return x