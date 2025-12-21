class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x=0
        y=0
        for i in nums1:
            if i in nums2:
                x+=1
        for j in nums2:
            if j in nums1:
                y+=1
        return [x,y]