from collections import Counter
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        a=set(words)
        b=Counter(words)
        x=0
        y=0
        for i in a:
            if i==i[::-1]:
                x+=(b[i]//2)
                if b[i]%2==1:
                    y=1
            else:
                if i[::-1] in a:
                    x+=min(b[i],b[i[::-1]])
                    b[i]=0
                    b[i[::-1]]=0
        return x*4+y*2