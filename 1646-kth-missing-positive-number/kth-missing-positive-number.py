class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        x=0
        for i in range(1,max(arr)+1):
            if i not in arr:
                x+=1
            if x==k:
                return i
        return max(arr)-x+k