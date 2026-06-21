class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a=[]
        for i in matrix:
            a.append(i[0])
        x=-1
        left=0
        right=len(a)-1
        while left<=right:
            mid=left+(right-left)//2
            if a[mid]==target:
                return True
            elif a[mid]>target:
                right=mid-1
            else:
                left=mid+1
        b=left-1
        left1=0
        right1=len(matrix[b])-1
        while left1<=right1:
            midd=left1+(right1-left1)//2
            if matrix[b][midd]==target:
                return True
            elif matrix[b][midd]>target:
                right1=midd-1
            else:
                left1=midd+1
        return False