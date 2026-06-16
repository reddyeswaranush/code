class Solution:
    def getSum(self, a: int, b: int) -> int:
        x=0xffffffff
        y=0x7fffffff
        while b:
            carry=((a&b)<<1)&x
            a=(a^b)&x
            b=carry
        return a if a<=y else ~(a^x)