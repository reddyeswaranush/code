class Solution:
    def isValid(self, word: str) -> bool:
        v=False
        u=False
        vovel="aeiouAEIOU"
        if len(word)<3:
            return False
        for i in word:
            if (not i.isnumeric()) and (not i.isalpha()):
                return False
            else:
                if i.isalpha():
                    if i in vovel:
                        v=True
                    else:
                        u=True
        if u and v:
            return True
        else:
            return False