class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        middle = 0

        while start <= end:

            middle = (start + end) // 2
            if nums[middle] == target:
                return middle

            if nums[start] > nums[middle] and (target < nums[middle] or target >= nums[start]):
                end = middle - 1
            elif nums[middle] > nums[end] and (target > nums[middle] or target <= nums[end]):
                start = middle + 1
            elif nums[middle] > target:
                end = middle - 1
            else:
                start = middle + 1
        
        return -1