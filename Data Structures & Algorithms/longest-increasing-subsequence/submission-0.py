class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
# for each number we have two options, either to accept it or not 

        lst = [0] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            count = 0
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    count = max(count, lst[j])
                
            lst[i] = count + 1
        
        return max(lst)