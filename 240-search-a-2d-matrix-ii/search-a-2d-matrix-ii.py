class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a = len(matrix)
        b = len(matrix[0])
        left = b - 1
        right = 0
        while right < a and left >= 0:
            mid = matrix[right][left]
            if mid == target:
                return True
            elif mid > target:
                left -= 1
            else:
                right += 1
        return False