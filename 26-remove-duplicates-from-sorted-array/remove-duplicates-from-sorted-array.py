class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a=set()
        nums1=nums[:]
        for i in nums:
            if i not in a:
                a.add(i)
            else:
                nums1.remove(i)
        nums[:]=nums1
        return len(nums)