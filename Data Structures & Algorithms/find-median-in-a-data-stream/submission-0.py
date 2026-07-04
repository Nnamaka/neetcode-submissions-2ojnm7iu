import heapq

class MedianFinder:

    def __init__(self):
        self.small_max_heap = []

        self.large_min_heap = []

    def addNum(self, num: int) -> None:
        # step 1: always push to max-heap first to see where it fits
        heapq.heappush(self.small_max_heap, -num)

        # step 2: Make sure every element in max-heap is <= every element
        if self.small_max_heap and self.large_min_heap:
            if (-self.small_max_heap[0]) > self.large_min_heap[0]:
                val = -heapq.heappop(self.small_max_heap)
                heapq.heappush(self.large_min_heap, val)

        # step 3: handle size balancing. Heaps must be equal size or max-heap can have 1 extra.
        if len(self.small_max_heap) > len(self.large_min_heap) + 1:
            val = -heapq.heappop(self.small_max_heap)
            heapq.heappush(self.large_min_heap, val)

        elif len(self.large_min_heap) > len(self.small_max_heap):
            val = heapq.heappop(self.large_min_heap)
            heapq.heappush(self.small_max_heap, -val)

    def findMedian(self) -> float:
        if len(self.small_max_heap) > len(self.large_min_heap):
            return float(-self.small_max_heap[0])

        return (-self.small_max_heap[0] + self.large_min_heap[0]) / 2.0
        
        