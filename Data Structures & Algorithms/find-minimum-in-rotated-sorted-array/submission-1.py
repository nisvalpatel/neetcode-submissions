class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if nums == None:
            return None

        start = 0
        end = len(nums) - 1
        middle = 0
        while start <= end:
            middle = (start + end) // 2
            
            if nums[start] > nums[middle]:
                end = middle
                start += 1
            elif nums[end] < nums[middle]:
                start = middle + 1
            else:
                end = middle - 1
        
        return nums[middle]


        return 
        
        


