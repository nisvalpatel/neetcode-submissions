class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0
        lst = []
        
        for i in range(amount):
            lst.append(1000000000)
        
        lst.append(0)

        
        for i in range(len(lst) - 2 , -1, -1):
            
            for coin in coins:
                if i + coin >= len(lst):
                    continue
                lst[i] = min(lst[i], lst[i + coin] + 1)

            
        if lst[0] >= 100000:
            return -1
        
        return lst[0]

        
        

        
