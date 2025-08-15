class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        a=bin(n)[2::]
        if len(a)%2!=0 and a.count('1')==1:
            return True
        else:
            return False