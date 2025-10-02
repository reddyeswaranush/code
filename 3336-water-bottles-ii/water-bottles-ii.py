class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        x = numBottles
        emptyBottles = numBottles

        while emptyBottles >= numExchange:
            emptyBottles -= numExchange
            numExchange += 1
            x += 1
            emptyBottles += 1
        return x