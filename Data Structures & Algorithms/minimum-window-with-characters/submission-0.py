from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        t_map = Counter(t)
        window = {}

        required = len(t_map)
        formed = 0

        left = 0
        min_len = float('inf')
        res = ""

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1


            if char in t_map and window[char] == t_map[char]:
                formed += 1


            while formed == required:

                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    res = s[left:right+1]


                left_char = s[left]
                window[left_char] -= 1

                if left_char in t_map and window[left_char] < t_map[left_char]:
                    formed -= 1

                left += 1

        return res