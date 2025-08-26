class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        a={}
        b={}
        for i in word1:
            if i not in a:
                a[i]=0
            a[i]+=1
        for i in word2:
            if i not in b:
                b[i]=0
            b[i]+=1
        for i in a:
            if i not in b:
                if a[i]>=4:
                    return False
            else:
                if abs(a[i]-b[i])>=4:
                    return False
        for i in b:
            if i not in a:
                if b[i]>=4:
                    return False
            else:
                if abs(b[i]-a[i])>=4:
                    return False
        return True