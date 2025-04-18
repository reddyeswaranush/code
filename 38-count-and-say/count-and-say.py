class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        a = "1"
        for _ in range(n - 1):
            x = ""
            i = 0
            while i < len(a):
                count = 1
                while i + 1 < len(a) and a[i] == a[i + 1]:
                    count += 1
                    i += 1
                x += str(count) + a[i]
                i += 1
            a = x
        return a