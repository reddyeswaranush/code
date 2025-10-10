class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        x = energy[-1]  
        for i in range(len(energy) - 1, -1, -1):
            if(i + k < len(energy)):
                energy[i] = energy[i] + energy[i + k]
            if(energy[i] > x):
                x = energy[i]
        return x