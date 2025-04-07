class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        x = total // 2
        dp = [False] * (x + 1)
        dp[0] = True
        for num in nums:
            for i in range(x, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[x]