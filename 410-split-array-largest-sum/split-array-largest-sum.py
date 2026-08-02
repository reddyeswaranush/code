class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left=max(nums)
        right=sum(nums)
        while left<right:
            mid=left+(right-left)//2
            a=0
            b=1
            for i in nums:
                if a+i>mid:
                    b+=1
                    a=i
                else:
                    a+=i
            if b>k:
                left=mid+1
            else:
                right=mid
        return left