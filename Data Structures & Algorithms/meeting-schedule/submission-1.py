"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1: return True
        intervalsArr = []
        for i in intervals:
            intervalsArr.append((i.start, i.end))
        intervalsArr = sorted(intervalsArr)
        prev = intervalsArr[0]
        print(intervalsArr)
        for i in range(1, len(intervalsArr)):
            if prev[1] > intervalsArr[i][0]: return False
            prev = intervalsArr[i]
        return True 