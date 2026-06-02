import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def getDistance(point1):
            return float(math.sqrt(((point1[0])**2) + ((point1[1])**2)))

        if len(points) == 0:
            return []

        minHeap = []

        for point in points:
            heapq.heappush(minHeap, (-1 * getDistance(point), point))

            if len(minHeap) > k:
                heapq.heappop(minHeap)



            
        
        return [i[1] for i in minHeap]







