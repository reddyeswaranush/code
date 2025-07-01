class Solution:
    def possibleStringCount(self, word: str) -> int:
        x=0
        i=0
        j=1
        n=len(word)
        while i<n:
            a=word[i]
            while j<n and word[j]==a:
                j=j+1
            x+=(j-i-1)
            i=j
        return x+1