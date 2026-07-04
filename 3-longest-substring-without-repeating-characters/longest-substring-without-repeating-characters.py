class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=set()
        left=0
        right=0
        max_len=0
        while right<len(s):
            if s[right] not in a:
                a.add(s[right])
                right+=1
            else:
                max_len=max(max_len,right-left)
                a.remove(s[left])
                left+=1
        max_len=max(max_len,right-left)
        return max_len