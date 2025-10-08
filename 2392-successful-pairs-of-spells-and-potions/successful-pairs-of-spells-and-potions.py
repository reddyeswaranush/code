from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        result = []

        for spell in spells:
            if spell >= success:
                result.append(len(potions))
            else:
                required_potion = (success + spell - 1) // spell
                idx = bisect_left(potions, required_potion)
                result.append(len(potions) - idx)
        
        return result