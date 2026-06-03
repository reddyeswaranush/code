class Solution:
    def possible(self, cap, weights, days):
        x=1
        cur=0
        for w in weights:
            if cur+w>cap:
                x+=1
                cur=0
            cur+=w
        return x<=days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        right=sum(weights)
        while left<=right:
            mid=left+(right-left)//2
            if self.possible(mid,weights,days):
                right=mid-1
            else:
                left=mid+1
        return left