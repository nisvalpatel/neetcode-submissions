class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        inNums = set()

        for n in nums:
            inNums.add(n)

        
        res = []
        
        for i in range(1, len(nums) + 1):
            if i not in inNums:
                res.append(i)

        return res
