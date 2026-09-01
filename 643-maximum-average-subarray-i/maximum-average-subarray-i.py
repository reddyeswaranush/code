class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        a=sum(nums[:k])
        maxx=a
        for i in range(k,len(nums)):
            a+=(nums[i]-nums[i-k])
            maxx=max(a,maxx)
        return maxx/k