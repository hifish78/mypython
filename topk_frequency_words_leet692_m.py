import collections
import heapq
class Solution:
    """
    要点：
    1）candidates.sort(key=lambda x: (-count[x], x))  wrong!!!
       dict_keys object has no attribute 'sort' !!!
       MUST use: candidates = sorted(candidates, key=lambda x : (-count[x], x)
    2) key=lambda x : (-count[x], x), 以count[x]从大到小 + x 从小到大排序！！！(用到了-count[X])
    3) Time Complexity: O(NlogN), where N is the length of words.
       We count the frequency of each word in O(N) time, then we sort the given words in
       O(NlogN) time. （NOT Good time complexity)
       Space Complexity: O(N), the space used to store our candidates.

    Python heapq
    heapq is a binary heap, with O(log n) push , O(log n) pop, O(n) heapify (建堆的复杂度是O(n))
    The algorithm you show takes O(n log n) to push all the items onto the heap,
    and then O((n-k) log n) to find the kth largest element.
    So the complexity would be O(n log n).

    Heap data structure is mainly used to represent a priority queue.
    1)smallest of heap element is popped(min heap)
    2)heap[0] element return the smallest element each time
    3)heapify(iterable) - convert the iterable into a heap in heap order
    4)heappush(heap, element)
    5)heappop(heap)
    """
    # Time Complexity: O(NlogK)
    # In Python, we improve this to O(N+klogN):
    # our heapq.heapify operation and counting operations are O(N),
    # and each of k heapq.heappop operations are O(logN).
    # Space Complexity: O(N)O(N), the space used to store our count.
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        heap = [(-v, k) for k, v in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]

    # NOT good solution O(NlogN)
    def topKFrequent2(self, words, k):
        if not words or k <= 0:
            return []
        count = collections.Counter(words)
        candidates = count.keys()
        candidates = sorted(candidates, key=lambda x: (-count[x], x))
        # wrong way below
        # list_count = sorted([(v, k) for k, v in count.items()], reverse=True)
        # res = [list_count[i][1] for i in range(k)]
        return candidates[:k]

sol = Solution()
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
print(sol.topKFrequent(words, k))

