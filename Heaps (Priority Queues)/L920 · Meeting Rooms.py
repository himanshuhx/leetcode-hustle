class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort(key = lambda a : a.start)
        for i in range(1, len(intervals)):
            if intervals[i-1].end > intervals[i].start:
                return False

        return True