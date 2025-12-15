class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        x=1
        cnt=1
        for i in range(1,len(prices)):
            if prices[i]==prices[i-1]-1:
                cnt+=1
            else:
                cnt=1
            x+=cnt
        return x