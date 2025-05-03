class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(x):
            min1 = min2 = 0
            for i in range(len(tops)):
                if tops[i] != x and bottoms[i] != x:
                    return float('inf')
                elif tops[i] != x:
                    min1 += 1
                elif bottoms[i] != x:
                    min2 += 1
            return min(min1, min2)

        ans = min(check(tops[0]), check(bottoms[0]))
        return ans if ans != float('inf') else -1