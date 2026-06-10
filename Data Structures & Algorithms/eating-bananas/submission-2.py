class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        #helper function to test whether the eating speed works

        def testing(k):
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / k)
            return total_hours <= h

                



        if len(piles) > h:
            return -1
        
        left = 1
        right = max(piles)
        ret = right

        while left <= right:

            #k is the middle
            k = (left + right) // 2

            if testing(k):
                ret = k
                right = k - 1
            else:
                left = k + 1
        
        return ret

        



