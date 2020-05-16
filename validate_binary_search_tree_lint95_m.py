class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

"""
如果是BST，那么中序序列一定是增序的。
需要一个额外的节点记录前一个节点，然后和当前节点的值比较大小
"""
class Solution:
    # Solution1
    def isValidBST(self, root):
        if root is None:
            return True
        stack = []
        res = []
        last_node = None
        while stack or root is not None:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                if last_node is not None and last_node.val >= node.val:
                    return False
                last_node = node
                root = node.right
        return True

    # Solution2:
    def isValidBST2(self, root):
        self.last_node = None
        self.is_valid = True
        self.inorder(root)
        return self.is_valid

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        if self.last_node is not None and self.last_node.val >= root.val:
            self.is_valid = False
            return  # add return here to allow more efficiency
        self.last_node = root
        self.inorder(root.right)

    # Solution3 (divided-conquer)
    def isValidBST3(self, root):
        is_bst, min_node, max_node = self.divide_conquer(root)
        return is_bst

    def divide_conquer(self, root):
        if root is None:
            return True, None, None
        left_is_bst, left_min, left_max = self.divide_conquer(root.left)
        right_is_bst, right_min, right_max = self.divide_conquer(root.right)

        if not left_is_bst or not right_is_bst:
            return False, None, None
        if left_max is not None and left_max.val >= root.val:
            return False, None, None
        if right_min is not None and right_min.val <= root.val:
            return False, None, None

        # is BST
        min_node = left_min if left_min is not None else root
        max_node = right_max if right_max is not None else root
        return True, min_node, max_node

