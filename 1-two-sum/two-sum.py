class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        n=len(nums)
        for i in range(n):
            if target-nums[i] in a:
                return [a[target-nums[i]],i]
            a[nums[i]]=i