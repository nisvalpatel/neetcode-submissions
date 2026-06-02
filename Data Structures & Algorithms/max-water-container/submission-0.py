class Solution:
    # we are given an array of heights
    # think of it as a bar graph such that it can act as walls for the bucket
    # the amount of water it can store will be the difference in indexes times the height
    # of min wall of the two

    # one way we can do this is by checking each wall we have with each other having
    # runtime of O(n^2)

    # we can do a two pointers starting at each end and basically closing in. the pointer
    # that moves in will be the one that is smaller out of the two. keep going until you reach
    # the middle and then have the largest value stored. boom thats it

    def maxArea(self, heights: List[int]) -> int:

        maxWater = 0
        left = 0
        right = len(heights) - 1

        while left <= right:
            maxWater = max(maxWater, (right - left) * min(heights[left], heights[right]))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxWater
        