from collections import Counter
from typing import List

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []
        n = len(nums)
        
        for i in range(n - k + 1):
            a = Counter(nums[i:i+k])
            top = sorted(a.items(), key=lambda p: (-p[1], -p[0]))
            b = 0
            for j in range(min(x, len(top))):
                b += top[j][0] * top[j][1]
            ans.append(b)
        
        return ans