from typing import List
import sys
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums or not k:
            return []

        dq = deque([])
        for i in range(k - 1):
            self.push(dq, nums, i)

        result = []
        for i in range(k - 1, len(nums)):
            self.push(dq, nums, i)
            result.append(nums[dq[0]])
            if dq[0] == i - k + 1:
                dq.popleft()

        return result

    def push(self, dq, nums, i):
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)

nums = [4,2,3,5,6,3]
k = 3
sol = Solution()
print(sol.maxSlidingWindow(nums, k))

# root = TreeNode(1)
# root.left = TreeNode(-5)
# root.right= TreeNode(3)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(2)
# root.right.left = TreeNode(-4)
# root.right.right = TreeNode(-5)


