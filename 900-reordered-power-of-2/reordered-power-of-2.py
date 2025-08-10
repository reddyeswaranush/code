class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        perms = {int(''.join(p)) for p in permutations(str(n)) if p[0] != '0'}
        for i in perms:
            if bin(i)[2::].count("1")==1:
                return True
        return False