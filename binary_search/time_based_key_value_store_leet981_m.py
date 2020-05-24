import collections
import bisect
class TimeMap:
    '''
    要点：
    1） 我们可以通过defaultdict将输入的 key:(value, timestamp) 存放到一个字典中，然后对相同对Key不同的timestamp 二分查找不大于给定的TIMESTAMP的VALUE 即可。
    2） 注意只有两个值的情况
        [(10, high), (20, low)] :
        if timestamp >= 20 (end point):  return 20, values[end][1]
        if 10 <= timestamp < 20 (between start point and end point): return 10, values[start][1]
        ir timestamp < 10 (start point): return ''
    3) Time Complexity: O(1)for each set operation, and O(logN) for each get operation, where N is the number of entries in the TimeMap.
       Space Complexity: O(N)O(N).
    '''
    # Solution1
    def __init__(self):
        self.data = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        self.data[key].append((timestamp, value))

    def get(self, key, timestamp):
        values = self.data.get(key, None)

        if values is None:
            return ''

        start, end = 0, len(values) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if timestamp == values[mid][0]:
                return values[mid][1]
            elif timestamp < values[mid][0]:
                end = mid
            else:
                start = mid

        if timestamp >= values[end][0]:
            return values[end][1]
        if timestamp < values[end][0] and timestamp >= values[start][0]:
            return values[start][1]
        return '' #timestamp < values[start][0]

    # Solution2 (using bisect, actually it is the same as 1)
    def get2(self, key, timestamp):
        if key not in self.data:
            return ''
        values = self.data.get(key)
        index = bisect.bisect(values, (timestamp, chr(255)))
        return values[index-1][1] if index - 1 >= 0 else ''


