class Solution:
    def minOperations(self, nums: List[int]) -> int:
        st = []
        c = 0
        for i in nums:
            while st and st[-1] > i:
                st.pop()
            if i == 0:
                continue
            if not st or st[-1] < i:
                st.append(i)
                c += 1
        return c