class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

"""
python也要写result type么？写result type 是个加分相么？
python因为可以返回多个返回值，所以不需要写result type
see: isBalanced2() && helper2()
"""

class ResultType:
    def __init__(self, isBalanced, max_depth):
        self.isBalanced = isBalanced
        self.max_depth = max_depth


class Solution:
    def isBalanced(self, root):
        if root is None:
            return True
        left = self.get_depth(root.left)
        right = self.get_depth(root.right)
        return abs(left - right) and self.isBalanced(root.left) and self.isBalanced(root.right)

    def get_depth(self, root):
        if root is None:
            return 0
        left = self.get_depth(root.left)
        right = self.get_depth(root.right)
        return max(left, right) + 1

    def isBalanced1(self, root):
        return self.helper(root).isBalanced

    def helper(self, root):
        if root is None:
            return ResultType(True, 0)

        left = self.helper(root.left)
        right = self.helper(root.right)

        # subtree not balance
        # ResultType(False, -1), -1 or other value works
        # return ResultType(False, max(left.max_depth, right.max_depth) + 1) works too
        if not left.isBalanced or not right.isBalanced:
            return ResultType(False, -1)
        # root not balance
        if abs(left.max_depth - right.max_depth) > 1:
            return ResultType(False, -1)
        return ResultType(True, max(left.max_depth, right.max_depth) + 1)

    def isBalanced2(self, root):
        return self.heper2(root)[0]

    def helper2(self, root):
        # isBalanced, maxDepth
        if root is None:
            return True, 0
        left = self.helper(root.left)
        right = self.helper(root.right)

        if not left[0] or not right[0]:
            return False, -1
        if abs(left[1] - right[1]) > 1:
            return False, -1
        return  True, max(left[1], right[1]) + 1







