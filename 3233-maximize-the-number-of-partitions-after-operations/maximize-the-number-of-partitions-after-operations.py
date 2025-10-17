class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        @cache
        def dfs(i, mask, changed):
            if i == len(s):
                return 1
            idx = ord(s[i]) - ord('a')
            new_mask = mask | (1 << idx)
            if new_mask.bit_count() > k:
                res = 1 + dfs(i + 1, (1 << idx), changed)
            else:
                res = dfs(i + 1, new_mask, changed)
            
            if not changed:
                if mask.bit_count() == k and (mask >> idx) & 1 == 0:
                    res = max(res, 1 + dfs(i + 1, (1 << idx), True))
                for x in range(26):
                    if (mask >> x) & 1:
                        continue
                    if x == idx:
                        continue
                    new_mask2 = mask | (1 << x)
                    if new_mask2.bit_count() > k:
                        res = max(res, 1 + dfs(i + 1, (1 << x), True))
                    else:
                        res = max(res, dfs(i + 1, new_mask2, True))
            return res
        
        return dfs(0, 0, False)