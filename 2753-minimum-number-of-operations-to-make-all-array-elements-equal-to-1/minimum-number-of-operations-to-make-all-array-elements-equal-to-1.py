from math import gcd
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        ones = sum(1 for x in nums if x == 1)
        if ones > 0:
            return n - ones

        g = 0
        for x in nums:
            g = gcd(g, x)
        if g > 1:
            return -1

        best = 10**9
        for i in range(n):
            cur = 0
            for j in range(i, n):
                cur = gcd(cur, nums[j])
                if cur == 1:
                    best = min(best, j - i + 1)
                    break

        return (best - 1) + (n - 1)