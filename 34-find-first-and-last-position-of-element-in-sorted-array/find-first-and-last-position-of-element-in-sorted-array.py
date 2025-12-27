class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def findFirst():
            low, high = 0, len(nums) - 1
            ans = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    ans = mid
                    high = mid - 1   # keep going left
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return ans

        def findLast():
            low, high = 0, len(nums) - 1
            ans = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    ans = mid
                    low = mid + 1   # keep going right
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return ans

        return [findFirst(), findLast()]