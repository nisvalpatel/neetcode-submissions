class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combinedList = sorted(zip(position, speed))

        # the formula to find hours to reach the location is
        # hours = 1.0 * (target - position) / speed

        stack = sorted(zip(position, speed))
        currHours = 0
        count = 0

        while len(stack) != 0:
            curr = stack.pop()
            if not (currHours >= 1.0 * (target - curr[0]) / curr[1]):
                count += 1
                currHours = 1.0 * (target - curr[0]) / curr[1]


        
        return count
            

        