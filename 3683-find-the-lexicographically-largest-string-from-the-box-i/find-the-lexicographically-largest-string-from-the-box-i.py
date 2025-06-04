class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

        n = len(word)
        ans = ""
        max_len = n - numFriends + 1
        for i in range(n):
            k = min(n - i, max_len)
            candidate = word[i:i + k]
            if candidate > ans:
                ans = candidate
        return ans