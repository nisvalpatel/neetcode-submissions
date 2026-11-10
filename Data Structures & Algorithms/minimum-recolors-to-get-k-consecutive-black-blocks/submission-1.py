class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        right = k - 1

        hash_map = {
            "W": 0,
            "B": 0,
        }

        for i in range(k):
            hash_map[blocks[i]] += 1


        min_count = hash_map["W"]

        while right < len(blocks):

            min_count = min(min_count, hash_map["W"])
            hash_map[blocks[left]] -= 1
            left += 1

            right += 1
            if right < len(blocks):
                hash_map[blocks[right]] += 1
            
    
            
        return min_count
            
