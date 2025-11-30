from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        rem = total_sum % p
        if rem == 0:
            return 0
        
        prefix_sum = 0
        min_len = len(nums)
        mod_dict = {0: -1}
        
        for i, num in enumerate(nums):
            prefix_sum += num
            current_mod = prefix_sum % p

            target = (current_mod - rem + p) % p

            if target in mod_dict:
                min_len = min(min_len, i - mod_dict[target])

            mod_dict[current_mod] = i
        
        return min_len if min_len < len(nums) else -1