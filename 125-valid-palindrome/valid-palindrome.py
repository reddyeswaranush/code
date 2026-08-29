class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=''
        "".join(s)
        for i in s:
            if i.isalpha() or i.isalnum():
                a+=i.lower()
        return a==a[::-1]