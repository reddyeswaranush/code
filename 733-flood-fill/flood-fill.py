class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        a = image[sr][sc]
        r,c = len(image),len(image[0])
        def search(i,j,grid):
            if i<0 or i>=r or j<0 or j>=c:
                return 
            if a != grid[i][j] or grid[i][j]==color:
                return
            grid[i][j] = color
            search(i-1,j,grid)
            search(i,j-1,grid)
            search(i+1,j,grid)
            search(i,j+1,grid)
        search(sr,sc,image)
        return image