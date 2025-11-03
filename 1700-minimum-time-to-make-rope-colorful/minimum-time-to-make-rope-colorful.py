class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        total = sum(neededTime)
        keep = 0
        i = 0
        n = len(colors)
        while i < n:
            j = i
            curr_max = neededTime[i]
            while j + 1 < n and colors[j + 1] == colors[i]:
                j += 1
                curr_max = max(curr_max, neededTime[j])
            keep += curr_max
            i = j + 1
        
        return total - keep