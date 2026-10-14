class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_distance = nums[0]

        for index in range(len(nums)):
            if index > max_distance:
                return False
            
            max_distance = max(max_distance, index + nums[index])

        
        return True