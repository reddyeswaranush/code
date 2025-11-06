class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            a = nums2.index(i)
            next_greater = -1
            for j in nums2[a+1:]:
                if j > i:
                    next_greater = j
                    break
            ans.append(next_greater)
        return ans