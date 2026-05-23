class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        a = set()
        n = len(nums)
        for i in range(n):
            left = i + 1
            right = n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    a.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1
        return list(a)