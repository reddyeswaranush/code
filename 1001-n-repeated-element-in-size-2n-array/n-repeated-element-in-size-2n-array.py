from collections import Counter

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        a = Counter(nums)
        b = len(nums) // 2
        return next(x for x in a if a[x] == b)