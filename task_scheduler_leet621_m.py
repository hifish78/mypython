
from collections import Counter
'''
https://www.youtube.com/watch?v=YCD_iYxyXoo
'''
class Solution:
    def leastInterval(self, tasks, n):
        d = Counter(tasks)
        counts = list(d.values())
        max_frequency = max(counts)
        ans = (max_frequency - 1) * (n + 1) + counts.count(max_frequency)
        return max(ans, len(tasks))