class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        n=len(grid)
        gridc=[]
        for i in range(len(grid[0])):
            a=[]
            for j in range(n):
                a.append(grid[j][i])
            gridc.append(a)
        min_row=0
        min_col=0
        max_row=0
        max_col=0
        for i in range(n):
            if 1 in grid[i]:
                min_row=i
                break
        for i in range(n-1,0,-1):
            if 1 in grid[i]:
                max_row=i
                break
        for i in range(len(gridc)):
            if 1 in gridc[i]:
                min_col=i
                break
        for i in range(len(gridc)-1,0,-1):
            if 1 in gridc[i]:
                max_col=i
                break
        return (max_row-min_row+1)*(max_col-min_col+1)