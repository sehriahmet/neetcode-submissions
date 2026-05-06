class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals = sorted(intervals)
        prev = 0
        flag = 0
        for curr in range(1, len(intervals)):
            if intervals[prev][1] > intervals[curr][0]:
                count += 1 
                temp = prev
                if intervals[prev][1] < intervals[curr][1]:
                    flag = 1 
            prev = curr
            if flag: 
                prev = temp
                flag = 0

        return count
                    
