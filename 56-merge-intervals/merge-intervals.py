class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals, key=lambda x:x[0])
        n=len(intervals)
        a=[]
        for i in intervals:
            if len(a)==0:
                a.append(i)
            else:
                if a[-1][1]>=i[0]:
                    a[-1][1]=max(a[-1][1],i[1])
                else:
                    a.append(i)
        return a