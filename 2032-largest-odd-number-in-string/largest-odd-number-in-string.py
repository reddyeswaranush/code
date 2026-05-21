class Solution:
    def largestOddNumber(self, num: str) -> str:
        num=num[::-1]
        n=len(num)
        for i in range(n):
            if int(num[i])%2!=0:
                return num[i:][::-1]
        return ""