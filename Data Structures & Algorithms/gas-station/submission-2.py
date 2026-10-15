class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        #edge case: not possible

        if sum(gas) < sum(cost):
            return -1
        
        curr_tank = 0
        start = 0
        for i in range(len(gas)):
            curr_tank += gas[i]
            curr_tank -= cost[i]
        
            if curr_tank < 0:
                start = i + 1
                curr_tank = 0
                continue

        return start
