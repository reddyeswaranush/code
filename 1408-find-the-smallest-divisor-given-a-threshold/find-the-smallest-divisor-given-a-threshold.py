class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        x=2**31-1
        left=1
        right=max(nums)
        while left<=right:
            mid=(left+right)//2
            a=0
            for i in nums:
                a+=math.ceil((i)/mid)
            if a<=threshold:
                right=mid-1    
                x=mid
            else:
                left=mid+1
        return x