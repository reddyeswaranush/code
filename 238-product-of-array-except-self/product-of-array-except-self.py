class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a=[]
        b=1
        zero=0
        for i in nums:
            if i==0:
                zero+=1
            else:
                b=b*i
        for i in nums:
            if zero==0:
                a.append(b//i)
            elif zero==1:
                if i!=0:
                    a.append(0)
                else:
                    a.append(b)
            else:
                a.append(0)
        return a