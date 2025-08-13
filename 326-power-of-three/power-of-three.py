class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        a=1162261467
        if n>0 and a%n==0:
            return True
        else:
            return False