from collections import Counter

class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.num1 = nums1
        self.num2 = nums2
        self.freq2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old = self.num2[index]
        self.freq2[old] -= 1
        if self.freq2[old] == 0:
            del self.freq2[old]
        self.num2[index] += val
        self.freq2[self.num2[index]] += 1

    def count(self, tot: int) -> int:
        return sum(self.freq2.get(tot - i, 0) for i in self.num1)


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)