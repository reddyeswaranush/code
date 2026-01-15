class Solution:
    def find(self, bars):
        bars.sort()
        longest = curr = 1
        for i in range(1, len(bars)):
            if bars[i] == bars[i - 1] + 1:
                curr += 1
                longest = max(longest, curr)
            else:
                curr = 1
        return longest
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        return((1 + min(self.find(hBars), self.find(vBars)))**2)