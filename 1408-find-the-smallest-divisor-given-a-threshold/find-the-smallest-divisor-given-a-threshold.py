class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left=1
        right=max(nums)
        while left<=right:
            mid=left+(right-left)//2
            a=0
            for i in nums:
                a+=i//mid
                if i%mid!=0:
                    a+=1
            if a<=threshold:
                right=mid-1
            else:
                left=mid+1
        return left