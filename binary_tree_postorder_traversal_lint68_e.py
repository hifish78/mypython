class Solution:
    def postorderTraversal(self, root):
        # write your code here
        res = []
        if root is None:
            return res
        self.postorder(root, res)
        return res

    def postorder(self, root, res):
        if root is None:
            return
        self.postorder(root.left, res)
        self.postorder(root.right, res)
        res.append(root.val)

    def postorderTraversal(self, root):
        res = []
        if root is None:
            return res
        stack = []

        # record the last visited node
        last_visited = None
        while stack or root is not None:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                node = stack[-1]
                if node.right is None or last_visited == node.right:
                    res.append(node.val)
                    last_visited = stack.pop()
                else:
                    root = node.right
        return res