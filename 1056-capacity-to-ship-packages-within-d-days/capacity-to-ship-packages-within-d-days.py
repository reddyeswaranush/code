class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        right=sum(weights)
        while left<right:
            mid=left+(right-left)//2
            a=0
            b=1
            for i in weights:
                if a+i>mid:
                    b+=1
                    a=i
                else:
                    a+=i
            if b>days:
                left=mid+1
            else:
                right=mid
        return left