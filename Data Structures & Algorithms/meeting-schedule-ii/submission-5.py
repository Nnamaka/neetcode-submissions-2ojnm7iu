"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        # step 1: Sort meetings by start time
        intervals.sort(key=lambda x: x.start)

        # step 2: Min-heap to store the end times of active meetings
        free_rooms = []

        # Add the end time of the first meeting
        heapq.heappush(free_rooms, intervals[0].end)

        # Step 3: Process remaining meetings
        for meeting in intervals[1:]:
            # if the room that frees up earliest is ready, reuse it
            if meeting.start >= free_rooms[0]:
                heapq.heappop(free_rooms)

            # Push the current meeting's end time (occupying a room)
            heapq.heappush(free_rooms, meeting.end)

        # The size of the heap is the minimum rooms required
        return len(free_rooms)

        