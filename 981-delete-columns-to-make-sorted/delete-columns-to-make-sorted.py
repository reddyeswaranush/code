class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        a=[]
        for i in range(len(strs[0])):
            b=''
            for j in strs:
                b+=j[i]
            a.append(b)
        print(a)
        x=0
        for i in a:
            if "".join(sorted(i))!=i:
                x+=1
        return x