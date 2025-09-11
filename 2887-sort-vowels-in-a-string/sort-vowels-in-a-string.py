class Solution:
    def sortVowels(self, s: str) -> str:
        a=['a','e','i','o','u']
        b=[]
        for i in s:
            if i.lower() in a:
                b.append(i)
        b.sort()
        x=[]
        y=0
        for i in s:
            if i.lower() in a:
                x.append(b[y])
                y+=1
            else:
                x.append(i)
        return "".join(x)