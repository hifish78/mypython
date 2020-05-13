class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def inorder_traversal(self, root):
        res = []
        if root is None:
            return res
        self.traverse(root, res)
        return res

    def traverse(self, root, res):
        if root is None:
            return
        self.traverse(root.left, res)
        res.append(root.val)
        self.traverse(root.right, res)

    def inorderTraversal(self, root):
        res = []
        if root is None:
            return res
        stack = []
        while stack or root is not None:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                res.append(node.val)
                root = node.right
        return res

        
