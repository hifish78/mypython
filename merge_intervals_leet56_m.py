class Solution:
    """
    要点：
    1) time complexity: O(nlogn)
       sort：intervals.sort(key=lambda x:x[0])
    2）space complexity: O(n)
    """
    def merge(self, intervals):
        if not intervals:
            return intervals
        intervals.sort(key=lambda x:x[0])
        res = []
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] > res[-1][1]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res

