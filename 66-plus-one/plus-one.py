class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x=''
        for i in digits:
            x+=str(i)
        x=str(int(x)+1)
        a=[]
        for i in x:
            a.append(int(i))
        return a