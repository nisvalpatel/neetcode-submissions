from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t:
            return ""

        needed = Counter(t)
        window = defaultdict(int)

        have = 0
        need = len(needed)

        left = 0
        res = [-1, -1]
        res_len = float("inf")

        for right in range(len(s)):
            char = s[right]
            window[char] += 1

            if char in needed and window[char] == needed[char]:
                have += 1

            while have == need:

                if right - left + 1 < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                left_char = s[left]
                window[left_char] -= 1

                if (
                    left_char in needed
                    and window[left_char] < needed[left_char]
                ):
                    have -= 1

                left += 1

        l, r = res

        return s[l:r + 1] if res_len != float("inf") else ""