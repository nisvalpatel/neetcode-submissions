class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return -1

        ans = nums[0] 
        curr = nums[0]
        for i in range(1, len(nums)):
            curr = max(curr + nums[i], nums[i])
            ans = max(ans, curr)
        
        return max(curr, ans)



        
