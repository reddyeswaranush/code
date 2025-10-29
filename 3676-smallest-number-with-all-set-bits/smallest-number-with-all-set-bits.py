class Solution:
    def smallestNumber(self, n: int) -> int:
        a=len(bin(n)[2:])
        return 2**a-1