from collections import deque
class Solution:
    """
    我们从双端队列的特点——头尾入手，定义该队列的头部必须是当前窗口内数值的最大值，这样我们就能获得结果了。
    如何实现？每次窗口移动，我们从队尾加入新增的数值，如果队尾数值小于它，那么抛出队尾数值，如此循环直到该新增数值找到它的位置，那些抛弃的数值并不重要，
    因为我们只要可能的最大值。当然，因为数值左边界移动，我们也要抛弃那些不在窗口内的数值，我们的队列保证了队头到队尾数值下标是递增顺序的，
    所以从队头抛出那些不应该在窗口内的数值就可以了。

    最后还有一个问题，因为我们需要记录数值下标才能从队头抛出不在窗口的元素，而且保存元素下标的话我们可以获得元素本身和下标两个信息，
    如果记录的不是下标，而是数字本身的话，如果有重复的数字，没有办法删除哪一个位置上的数字

    两种情况出窗：
    1）从对头出窗， deque非空，队头的下标 == i -K
    2）从队尾出窗：如果队尾数值小于它，那么抛出队尾数值，如此循环直到该新增数值找到它的位置

    和 window_sum_lint604_e.py 比较
    """
    def maxSlidingWindow(self, nums, k):
        if not nums or k <= 0:
            return []
        dq = deque()
        res = []

        for i in range(k - 1):
            self.push(dq, nums, i)

        for i in range(k-1, len(nums)):
            self.push(dq, nums, i)
            res.append(dq, nums, i)
            if dq[0] == i - k + 1: # you can give an example to calculate boundary
                dq.popleft()
            return res

    def push(self, dq, nums, i):
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)

    def maxSlidingWindow1(self, nums, k):
        # write your code here
        if not nums or k <= 0:
            return []

        def clean_deque(i):
            # remove indexes of elements not from sliding window
            if dq and dq[0] == i - k:
                dq.popleft()
            # remove from deque indexes from all elements which are smaller than current element nums[i]
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()

        result = []
        dq = deque()
        max_idx = 0

        # init deque and result
        for i in range(k):
            # 出window
            clean_deque(i)
            # 进window
            dq.append(i)
            # compute max in nums[:k]
            if nums[i] > nums[max_idx]:
                max_idx = i
        result.append(nums[max_idx])

        # build result
        for i in range(k, len(nums)):
            clean_deque(i)
            dq.append(i)
            result.append(nums[dq[0]])
        return result

    # 复杂度不好，超时
    def maxSlidingWindow2(self, nums, k):
        # write your code here

        if not nums or k <= 0:
            return []

        res = []
        res.append(max(nums[:k]))

        for i in range(k, len(nums)):
            val = max(nums[i - k + 1:i + 1])
            res.append(val)
        return res

