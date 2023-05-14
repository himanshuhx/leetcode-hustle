
class Solution:
    def minMeetingRooms(self, intervals):
        start = sorted([interval.start for interval in intervals])
        end = sorted([interval.end for interval in intervals])

        res = count = 0
        i, j = 0, 0
        while i < len(start):
            if start[i] < end[j]:
                i += 1
                count += 1
            else:
                j += 1
                count -= 1
            res = max(res, count)
        return res
