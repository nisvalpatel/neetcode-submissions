from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        if not s:
            return 0
        if len(s) == 1:
            return 1

        char_map = defaultdict(int)
        char_map[s[0]] += 1
        char_map[s[1]] += 1   # ✅ add this

        left = 0
        right = 1
        max_counter = 1

        while right < len(s):
            
            freq_val = max(char_map, key=char_map.get)

            # ❗ fix window size formula + decrement
            if (right - left + 1) - char_map[freq_val] > k:
                char_map[s[left]] -= 1   # ✅ FIXED
                left += 1
                continue

            max_counter = max((right - left + 1), max_counter)

            right += 1
            if right < len(s):
                char_map[s[right]] += 1

        return max_counter
        