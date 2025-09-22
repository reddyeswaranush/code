from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        a=Counter(nums)
        b=0
        for i in a:
            if a[i]>b:
                b=a[i]
        x=0
        print(b)
        for i in a:
            if a[i]==b:
                x+=b
        return x