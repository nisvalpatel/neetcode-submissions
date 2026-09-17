import heapq
class MedianFinder:

    def __init__(self):
        self.max_heap = []    #left side
        self.min_heap = []    #right side


    def addNum(self, num: int) -> None:
        if self.max_heap == []:
            heapq.heappush_max(self.max_heap, num)
            return
        
        
        if len(self.min_heap) < len(self.max_heap):

            if self.max_heap[0] > num:
                temp = heapq.heappop_max(self.max_heap)
                heapq.heappush_max(self.max_heap, num)
                heapq.heappush(self.min_heap, temp)    
            else:
                heapq.heappush(self.min_heap, num)
        else:
            if self.min_heap[0] < num:
                temp = heapq.heappop(self.min_heap)
                heapq.heappush(self.min_heap, num)
                heapq.heappush_max(self.max_heap, temp) 
            
            else: 
                heapq.heappush_max(self.max_heap, num)
            

    def findMedian(self) -> float:
        if (len(self.max_heap) + len(self.min_heap)) % 2 == 0:
            return (self.max_heap[0] + self.min_heap[0]) / 2
        
        return self.max_heap[0]
        