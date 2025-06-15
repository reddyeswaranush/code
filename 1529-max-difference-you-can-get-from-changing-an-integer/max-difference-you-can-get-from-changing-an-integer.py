class Solution:
    def maxDiff(self, num: int) -> int:
        a=str(num)
        for i in range(len(a)):
            if i==0 and int(a[i])!=1:
                mi=int(a.replace(a[i],'1'))
                break
            elif i==len(a)-1:
                mi=num
            elif i!=0:
                if int(a[i])==1 or int(a[i])==0:
                    continue
                else:
                    mi=int(a.replace(a[i],'0'))
                    break
        for i in range(len(a)):
            if int(a[i])!=9:
                ma=int(a.replace(a[i],'9'))
                break
            elif i==len(a)-1:
                ma=num
        return ma-mi