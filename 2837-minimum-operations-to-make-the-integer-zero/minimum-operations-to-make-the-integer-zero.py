class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for i in range(1,61):
            a=num1-i*num2
            if a<0:
                break
            elif a>=i and bin(a)[2:].count('1')<=i:
                return i
        return -1