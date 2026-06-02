class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        start_prev1 = 0
        start_prev2 = 0

        end_prev1 = 0
        end_prev2 = 0

        for i in range(len(nums) - 1):
            curr = max(start_prev1, start_prev2 + nums[i])
            start_prev2 = start_prev1
            start_prev1 = curr 

            curr = max(end_prev1, end_prev2 + nums[i + 1])
            end_prev2 = end_prev1
            end_prev1 = curr
        
        return max(start_prev1, end_prev1)


