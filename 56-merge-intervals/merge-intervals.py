class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals, key=lambda x:x[0])
        n=len(intervals)
        a=[]
        for i in range(n):
            if len(a)==0:
                a.append(intervals[i])
            else:
                if a[-1][1]>=intervals[i][0]:
                    a[-1][1]=max(a[-1][1],intervals[i][1])
                else:
                    a.append(intervals[i])
        return a