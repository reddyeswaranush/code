class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        a=text.split()
        b=list(brokenLetters)
        x=0
        for i in a:
            y=True
            for j in i:
                if j in b:
                    y=False
                    break
            if y:
                x+=1
        return x