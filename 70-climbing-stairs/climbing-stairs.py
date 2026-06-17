class Solution:
    def climbStairs(self, n: int) -> int:
        a = {}
        def help(x):
            if x<=1:
                return 1
            if x in a:
                return a[x]
            a[x]=help(x-1)+help(x-2)
            return a[x]
        return help(n)