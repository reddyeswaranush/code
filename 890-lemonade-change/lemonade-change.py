class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        x_5=0
        x_10=0
        for i in bills:
            if i==5:
                x_5+=5
            else:
                if i==10:
                    if x_5>=5:
                        x_5-=5
                        x_10+=10
                    else:
                        return False
                else:
                    if x_5>=5 and x_10>=10:
                        x_5-=5
                        x_10-=10
                    elif x_5>=15:
                        x_5-=15
                    else:
                        return False
        return True