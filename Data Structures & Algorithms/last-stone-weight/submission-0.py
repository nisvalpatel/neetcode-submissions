import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        if not stones:
            return 0
        
    
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            first = first - second
            heapq.heappush(stones, first)
        
        if len(stones) > 0:
            return -1 * heapq.heappop(stones)  
        return 0


