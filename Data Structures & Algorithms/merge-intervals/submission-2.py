class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        result = []
        result.append(intervals[0])
        j = 1

        while j<len(intervals):
            min1 = result[-1][0]
            max1 = result[-1][1]

            min2 = intervals[j][0]
            max2 = intervals[j][1]

            if max1>=min2:
                result.pop()
                result.append([min1, max(max1, max2)]) 
            else:
                result.append(intervals[j])

            print(j, intervals[j], min1, max2)

            j+=1
        return result
            
