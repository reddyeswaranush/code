class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        x=numBottles
        while numBottles//numExchange>0:
            a=numBottles//numExchange
            x+=a
            numBottles=a+numBottles%numExchange
        return x
