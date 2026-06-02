import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap_ = nums
        heapq.heapify(self.heap_)

        while len(self.heap_) > k:
            heapq.heappop(self.heap_)

        self.max_ = k

    def add(self, val: int) -> int:
        if len(self.heap_) < self.max_:
            heapq.heappush(self.heap_, val)
            return self.heap_[0]
        
        temp = heapq.heappop(self.heap_)
        heapq.heappush(self.heap_, max(temp, val))
        return self.heap_[0]

