class Solution:
    def kthCharacter(self, k: int) -> str:
        x="a"
        while len(x)<k:
            a=""
            for i in x:
                if i=="z":
                    a+="a"
                else:
                    a+=chr(ord(i)+1)
            x+=a
        return x[k-1]