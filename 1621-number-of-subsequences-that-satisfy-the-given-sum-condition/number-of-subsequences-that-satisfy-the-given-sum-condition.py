class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        x = 0
        for i in range(len(nums)):
            s,e = i,len(nums)-1
            mid = (s+e)//2
            while s<=e:
                if nums[i]+nums[mid]<=target:
                    s = mid + 1
                elif nums[i]+nums[mid]>target:
                    e = mid - 1
                mid = (s+e)//2
            if e>=i:
                x+=2**(e-i)
        return x % (10**9 + 7)