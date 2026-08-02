class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low=max(nums)
        high=sum(nums)
        while low<high:
            mid=low+(high-low)//2
            a=0
            split=1
            for i in nums:
                if a+i>mid:
                    split+=1
                    a=i
                else:
                    a+=i
            if split>k:
                low=mid+1
            else:
                high=mid
        return low