class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        a = [[num] for num in nums]
        for i in range(n):
            for j in range(i):
                if (nums[i] % nums[j]) == 0 and len(a[i]) < len(a[j]) + 1:
                    a[i] = a[j] + [nums[i]]
                    
        return max(a, key=len)