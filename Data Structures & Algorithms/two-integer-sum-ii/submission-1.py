class Solution:
    # given array of ints in increasing order so 0 -> n where n >= 0
    # return two values [index1, index 2] that are not equal and also index1 < index 2
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        index1 = 0
        index2 = len(numbers) - 1

        while index1 <= index2:
            if numbers[index1] + numbers[index2] > target:
                index2 -= 1
            elif numbers[index1] + numbers[index2] < target:
                index1 += 1
            else:
                return [index1 + 1, index2 + 1]

        
        return [-1,-1]
