class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        a=str(bin(n)[2:])
        if a.count('1')==1:
            return True
        else:
            return False