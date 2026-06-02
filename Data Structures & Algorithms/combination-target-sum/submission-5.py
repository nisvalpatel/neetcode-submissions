class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        if not nums:
            return []
        ret_list = []

        def recursive_helper(curr_list, index, curr_sum):
            if index >= len(nums):
                return 
            new_sum = nums[index] + curr_sum

            if new_sum > target:
                return
            
            curr_list.append(nums[index])
            if new_sum == target:
                ret_list.append(curr_list.copy())
                curr_list.pop()
                return
            
            recursive_helper(curr_list, index, new_sum) #repeating the same value
            for i in range(index, len(nums)):
                recursive_helper(curr_list, i + 1, new_sum) #choosing the next value
            curr_list.pop()
            return
        
    
        for i in range(len(nums)):
            curr_list = []
            recursive_helper(curr_list, i, 0)

        return ret_list
        