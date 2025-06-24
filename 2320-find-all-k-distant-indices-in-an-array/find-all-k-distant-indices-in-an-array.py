class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        x=set()
        n=len(nums)
        for i in range(n):
            for j in range(n):
                if nums[j]==key and abs(i-j)<=k:
                    x.add(i)
        return list(x)