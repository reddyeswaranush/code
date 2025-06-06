class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prefix = 0
        min_prefix = 0
        max_prefix = 0
        
        for diff in differences:
            prefix += diff
            min_prefix = min(min_prefix, prefix)
            max_prefix = max(max_prefix, prefix)
        
        return max(0, (upper - lower) - (max_prefix - min_prefix) + 1)