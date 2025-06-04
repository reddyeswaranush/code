class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)
        x = []
        
        if n == numFriends:
            return max(word)
        elif numFriends == 1:
            return word
        else:
            maxlen = n - numFriends + 1
            for i in range(n):
                x.append(word[i:i + maxlen])
        return max(x)