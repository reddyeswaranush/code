class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        x = [words[0]]
        n = len(words)
        def com(word1: str, word2: str) -> bool:
            freq = [0] * 26
            for ch in word1:
                freq[ord(ch) - ord("a")] += 1
            for ch in word2:
                freq[ord(ch) - ord("a")] -= 1
            return all(x == 0 for x in freq)

        for i in range(1, n):
            if com(words[i], words[i - 1]):
                continue
            x.append(words[i])
        return x