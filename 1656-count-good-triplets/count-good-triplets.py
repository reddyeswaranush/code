class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        x=0
        n=len(arr)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if abs(arr[i] - arr[j])<=a and abs(arr[j] - arr[k])<=b and abs(arr[k] - arr[i])<=c:
                        x+=1
        return x