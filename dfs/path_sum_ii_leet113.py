# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root is None:
            return []

        res = []
        self.dfs(root, sum, [], res)
        return res

    def dfs(self, root, sum, item, res):
        if root is None:
            return

        if root.left is None and root.right is None and sum == root.val:
            item.append(root.val)
            res.append(list(item))
            item.pop()
            return

        item.append(root.val)
        self.dfs(root.left, sum - root.val, item, res)
        self.dfs(root.right, sum - root.val, item, res)
        item.pop()
