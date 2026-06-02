class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        if start == end:
            return True 
        s = s.lower()

        while start < end:
            if not s[start].isalnum():
                start += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue
            if s[end] != s[start]:
                return False
            end -= 1
            start += 1
        return True