class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #The strategy for this problem is to basically have two 
        # pointers such that the left will point to the lowest value as
        # of now while the right parses right. If right runs into larger 
        # values than left, it will baically keep checking and comparing
        # to the "max profit", if there are  lefts and rights found such
        # that are greater than max profit, max profit gets replaced. you
        # keep going until right reaches the end of the list. as a result,
        # the runtime will be O(n)

        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            if prices[right] > prices[left]:
                max_profit = max(max_profit, prices[right] - prices[left])
            if prices[right] < prices[left]:
                left = right
            right += 1
        return max_profit