class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x=[]
        for i in nums1:
            a=False
            b=False
            for j in nums2:
                if i==j:
                    a=True
                if a==True and j>i:
                    x.append(j)
                    b=True
                    break
            if b==False:
                x.append(-1)
        return x