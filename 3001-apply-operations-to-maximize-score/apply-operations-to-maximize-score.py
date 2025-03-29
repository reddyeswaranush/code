@cache
def prime_score(num: int) -> int:
    score = 0
    if num % 2 == 0:
        score += 1
        while num % 2 == 0:
            num //= 2
    for p in range(3, int(sqrt(num)) + 1, 2):
        if num % p == 0:
            score += 1
            while num % p == 0:
                num //= p
    if num > 1:
        score += 1
    return score


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        scores = [prime_score(num) for num in nums] + [float('inf')]

        lefts = [-1] * n
        stack = []
        for i in range(n):
            while stack and scores[stack[-1]] < scores[i]:
                stack.pop()
            lefts[i] = stack[-1] if stack else -1
            stack.append(i)
        
        rights = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and scores[stack[-1]] <= scores[i]:
                stack.pop()
            rights[i] = stack[-1] if stack else n
            stack.append(i)

        sorted_nums = sorted(((num, i) for i, num in enumerate(nums)), reverse=True)
        
        ans = 1
        for num, i in sorted_nums:
            count = (i - lefts[i]) * (rights[i] - i)
            if k == 0:
                break
            power = min(k, count)
            ans = (ans * pow(num, power, MOD)) % MOD
            k -= power
        
        return ans