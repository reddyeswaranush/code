class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        a={0:1}
        b=0
        ans=0
        for i in nums:
            b+=i
            if b-k in a:
                ans+=a[b-k]
            if b not in a:
                a[b]=0
            a[b]+=1
        return ans