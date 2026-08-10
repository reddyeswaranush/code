class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x=[]
        for i in nums1:
            a=nums2[:]
            maxx=-1
            while a[-1]!=i:
                b=a.pop()
                if b>i:
                    maxx=b
            x.append(maxx)
        return x