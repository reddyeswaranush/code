class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        a=sum(apple)
        capacity=sorted(capacity,reverse=True)
        x=0
        for i in range(len(capacity)):
            x+=capacity[i]
            if x>=a:
                return i+1