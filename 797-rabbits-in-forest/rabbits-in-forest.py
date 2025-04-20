class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        a={}
        for i in answers:
            if i not in a:
                a[i]=0
            a[i]+=1
        x=0
        for i in a:
            if a[i]<=i+1:
                x+=i+1
            else:
                b=a[i]//(i+1)
                r=a[i]%(i+1)
                if r==0:
                    x+=(i+1)*b
                else:
                    x+=(i+1)*(b+1)
        return x