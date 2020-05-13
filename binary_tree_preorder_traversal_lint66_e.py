class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
Python stack usage:
Python Stack:  list is used as stack 
stack =  [ ]
stack.append()
stack.pop()
len(stack) != 0  <==> stack 
No “add” and NO “put"

在python中， None, False, 空字符串‘’， 0， 空列表[],  空字典{ },  空元组（） 都相当于False
>>> x = []
>>> not x
True

>>> x == None
False
>>> not x
True

>>> x is None
False
>>> not x
True

也许你是想判断x是否为None，但是却把`x==[]`的情况也判断进来了，此种情况下将无法区分。
`if x is not None`是最好的写法，清晰，不会出现错误，以后坚持使用这种写法。

"""
class Solution:
    def preorder_traversal(self, root):
        res = []
        self.traverse(root, res)
        return res

    def traverse(self, root, res):
        if root is None:
            return
        res.append(root.val)
        self.traverse(root.left, res)
        self.traverse(root.right, res)

    def preorder_traversal_norecursion(self, root):
        res = []
        if root is None:
            return []
        stack = []
        while stack or root is not None:
            if root is not None:
                res.append(root.val)
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                root = node.right
        return res

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




