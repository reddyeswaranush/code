class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        if len(s)%k!=0:
            return False
        a={}
        b={}
        c=len(s)
        k=c//k
        i=0
        j=0
        while i<c:
            if s[i:i+k] not in a:
                a[s[i:i+k]]=0
            a[s[i:i+k]]+=1
            i=i+k
        while j<c:
            if t[j:j+k] not in b:
                b[t[j:j+k]]=0
            b[t[j:j+k]]+=1
            j=j+k
        print(a)
        print(b)
        return a==b