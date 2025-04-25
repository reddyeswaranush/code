from collections import defaultdict
from typing import List
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        count = [0] * (n + 1) 
        for i in range(n):
            count[i + 1] = count[i] + (1 if nums[i] % modulo == k else 0)
        a = defaultdict(int)
        a[0] = 1
        x = 0
        for i in range(1, n + 1):
            cur = count[i] % modulo
            target = (cur - k + modulo) % modulo
            x += a[target]
            a[cur] += 1
        return x