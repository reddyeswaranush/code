from collections import Counter
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        x=[]
        a=Counter(digits)
        for i in range(100,999):
            b=Counter(list(map(int,str(i))))
            c=True
            for j in b:
                if b[j]>a[j]:
                    c=False
            if c and i%2==0:
                x.append(i)
        return x