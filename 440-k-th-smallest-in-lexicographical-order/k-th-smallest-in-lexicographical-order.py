class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        x = 1
        k -= 1

        while k > 0:
            steps = 0
            first = x
            last = x

            while first <= n:
                steps += min(last, n) - first + 1
                first *= 10
                last = last * 10 + 9

            if steps <= k:
                x += 1
                k -= steps
            else:
                x *= 10
                k -= 1
        return x