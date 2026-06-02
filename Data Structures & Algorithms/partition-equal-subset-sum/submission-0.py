class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        #base case where odd total_sum
        if (sum(nums) % 2 == 1):
            return False
        half_sum = sum(nums) / 2

        def dfs(curr_sum, curr):
            if curr_sum > half_sum:
                return False

            if curr_sum == half_sum:
                return True

            # we are checking if we reached end of the array
            if curr >= len(nums) - 1:
                return False
            
            if dfs(curr_sum + nums[curr], curr + 1) or dfs(curr_sum, curr + 1):
                return True
            else:
                return False
        
        return dfs(0, 0)

        

