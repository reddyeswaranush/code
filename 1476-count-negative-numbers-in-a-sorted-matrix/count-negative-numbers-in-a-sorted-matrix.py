class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        x=0
        for i in grid:
            low=0
            high=len(i)-1
            last_nos=-1
            while low<=high:
                mid=(low+high)//2
                if i[mid]<0:
                    last_nos=mid
                    high=mid-1
                else:
                    low=mid+1
            if last_nos!=-1:
                x+=(len(i)-last_nos)
        return x