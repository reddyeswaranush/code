from collections import Counter
class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        def isprime(n):
            if n==1:
                return False
            for i in range(2,n):
                if n%i==0:
                    return False
            return True
        a=Counter(nums)
        for i in a:
            if isprime(a[i]):
                return True
        return False