class Solution:
    def search(self, nums: List[int], target: int) -> int:

        lower = 0
        upper = len(nums) - 1
        if nums[upper] == target:
            return upper
        elif nums[lower] == target:
            return lower
        
        while lower != upper:
            middle = (int)((upper + lower) / 2 )
            if (abs(lower - upper) <= 1):
                break
            if (nums[middle] == target):
                return middle
            elif (nums[middle] > target):
                upper = middle
            else:
                lower = middle

        return -1