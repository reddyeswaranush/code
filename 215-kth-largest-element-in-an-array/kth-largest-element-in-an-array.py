class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        a=sorted(nums)[::-1]
        return a[k-1]