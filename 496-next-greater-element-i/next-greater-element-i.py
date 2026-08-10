class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a={}
        b=[]
        for i in range(len(nums2)-1,-1,-1):
            while b and b[-1]<nums2[i]:
                b.pop()
            if b:
                a[nums2[i]]=b[-1]
            else:
                a[nums2[i]]=-1
            b.append(nums2[i])
        x=[]
        for i in nums1:
            x.append(a[i])
        return x