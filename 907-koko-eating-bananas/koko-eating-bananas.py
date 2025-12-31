class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        x=high
        while low<=high:
            mid=(low+high)//2
            hours=0
            for i in piles:
                hours+=(i+mid-1)//mid
            if hours<=h:
                x=mid
                high=mid-1
            else:
                low=mid+1
        return x