class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Pass 1: mark seen values by negating nums[value-1]
        for num in nums:
            idx = abs(num) - 1      # use abs() since it may already be negative
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        # Pass 2: positive slots => that index+1 was never seen
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res
