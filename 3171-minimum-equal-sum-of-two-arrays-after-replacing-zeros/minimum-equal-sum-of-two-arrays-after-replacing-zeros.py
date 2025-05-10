class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        a=sum(nums1)+nums1.count(0)
        b=sum(nums2)+nums2.count(0)
        if (a<b and 0 not in nums1) or (b<a and 0 not in nums2):
            return -1
        else:
            return max(a,b)