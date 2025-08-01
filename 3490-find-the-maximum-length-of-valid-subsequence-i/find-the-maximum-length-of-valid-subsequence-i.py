class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        x = 0
        for pattern in [[0, 0], [0, 1], [1, 0], [1, 1]]:
            cnt = 0
            for num in nums:
                if num % 2 == pattern[cnt % 2]:
                    cnt += 1
            x = max(x, cnt)
        return x