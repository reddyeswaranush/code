class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod, runs, prev, cnt = 10**9 + 7, [], word[0], 1
        for ch in word[1:]:
            if ch == prev:
                cnt += 1
            else:
                runs.append(cnt)
                prev, cnt = ch, 1

        runs.append(cnt)
        total = 1
        for r in runs:
            total = total * r % mod

        m = len(runs)
        if m > k:
            return total
            
        dp = [1] + [0] * (k - 1)
        for r in runs:
            pref, s, r = [0] * k, 0, min(r, k)
            for i in range(k):
                s = (s + dp[i]) % mod
                pref[i] = s
            new = [0] * k
            for j in range(1, k):
                left = j - 1 - r
                val = pref[j - 1] - (pref[left] if left >= 0 else 0)
                new[j] = val % mod
            dp = new

        invalid = sum(dp) % mod
        return (total - invalid) % mod