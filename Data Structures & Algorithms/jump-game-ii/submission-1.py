class Solution:
    def jump(self, nums: List[int]) -> int:

        farthest = 0
        current_end = 0
        count = 0

        for i in range(0, len(nums) - 1):
            farthest = max(farthest, nums[i] + i)

            if current_end <= i:
                count += 1
                current_end = farthest
        
        return count