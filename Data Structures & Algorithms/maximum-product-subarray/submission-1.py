class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        ret = nums[0]
        minimum = 1
        maximum = 1

        for num in nums:

            if num < 0:
                temp = minimum
                minimum = maximum
                maximum = temp
                
            minimum = min(num, num*minimum)
            maximum = max(num, num*maximum)

            ret = max(maximum, ret)

        
        return ret
            

