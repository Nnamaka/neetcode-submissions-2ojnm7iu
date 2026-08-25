class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # step 1: Sort intervals by their END times (x[1])
        intervals.sort(key=lambda x: x[1])

        removals = 0
        prev_end = float('-inf')

        for start, end in intervals:
            # if the current interval starts after or when the previous ends, no overlap
            if start >= prev_end:
                prev_end = end
            else:
                # overlap detected: greedily remove the current inerval
                removals += 1
        return removals