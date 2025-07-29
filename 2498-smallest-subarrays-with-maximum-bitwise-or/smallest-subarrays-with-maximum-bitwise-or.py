class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [1]

        n = len(nums)
        res = []
        maxOR = [0] * n
        maxOR[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            maxOR[i] = maxOR[i + 1] | nums[i]
        
        bit = [0] * 32

        def check():
            res = 0 
            for i in range(32):
                if bit[i]:
                    res |= (1 << i)
            return res 

        def setBit(x):
            for i in range(32):
                bit[i] += (x >> i) & 1  

        def clearBit(x):
            for i in range(32):
                bit[i] -= (x >> i) & 1  

        j = 0 
        for i in range(n):
            if maxOR[i] == 0:
                res.append(1)
                continue 
                
            while j < n and check() != maxOR[i]:
                setBit(nums[j])
                j += 1
            res.append(j - i)
            clearBit(nums[i])
        
        return res