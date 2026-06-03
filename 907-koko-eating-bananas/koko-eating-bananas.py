class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        while left<=right:
            mid=left+(right-left)//2
            a=0
            for i in piles:
                a+=(i//mid)
                if i%mid!=0:
                    a+=1
            if a<=h:
                right=mid-1
            else:
                left=mid+1
        return left