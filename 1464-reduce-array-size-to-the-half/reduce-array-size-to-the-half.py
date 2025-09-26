from collections import Counter
from typing import List

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = Counter(arr)
        counts = sorted(freq.values(), reverse=True)
        
        removed, total, half = 0, 0, len(arr) // 2
        for c in counts:
            total += c
            removed += 1
            if total >= half:
                return removed