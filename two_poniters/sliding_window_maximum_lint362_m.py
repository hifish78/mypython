class Solution:
    """
    我们从双端队列的特点——头尾入手，定义该队列的头部必须是当前窗口内数值的最大值，这样我们就能获得结果了。
    如何实现？每次窗口移动，我们从队尾加入新增的数值，如果队尾数值小于它，那么抛出队尾数值，如此循环直到该新增数值找到它的位置，
    那些抛弃的数值并不重要，因为我们只要可能的最大值。
    当然，因为数值左边界移动，我们也要抛弃那些不在窗口内的数值，
    我们的队列保证了队头到队尾数值下标是递增顺序的，所以从队头抛出那些不应该在窗口内的数值就可以了。
    """