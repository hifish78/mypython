# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """
class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.peek_val = None

    def peek(self):
        if self.peek_val is None:
            # NOT return self.iterator.next()
            #return self.iterator.next()
            self.peek_val = self.iterator.next()
        return self.peek_val

    # NOT return self.peek_val directly, need to set to None
    def next(self):
        if self.peek_val is not None:
            tmp = self.peek_val
            self.peek_val = None
            return tmp
        return self.iterator.next()

    def hasNext(self):
        if self.peek_val is not None:
            return True
        return self.iterator.hasNext()