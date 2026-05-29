class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        x=[]
        for i in asteroids:
            if len(x)==0:
                x.append(i)
            elif (x[-1]<0 and i<0) or (x[-1]>0 and i>0):
                x.append(i)
            elif x[-1]<0 and i>0:
                x.append(i)
            else:
                b=False
                while x and (x[-1]>0 and i<0):
                    a=x.pop()
                    if a==-i:
                        b=True
                        break
                    elif a>-i:
                        i=a
                if not b:
                    x.append(i)
        return x