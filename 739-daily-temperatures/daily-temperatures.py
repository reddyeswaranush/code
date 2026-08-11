class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        x=[]
        for i in range(len(temperatures)-1,-1,-1):
            while stack and temperatures[stack[-1]]<=temperatures[i]:
                stack.pop()
            if stack:
                x.append(stack[-1]-i)
            else:
                x.append(0)
            stack.append(i)
        return x[::-1]