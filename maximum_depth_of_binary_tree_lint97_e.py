class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """

    """
    遍历是指沿着某条搜索路线，依次对树中每个结点均做一次且仅做一次访问，主要思想就是访问所有元素不重不漏，是否需要返回值需要看具体题目
    分治是将问题分解成若干小问题，解决小问题，合起来之后会解决大问题，所以一般来讲分治会用到小问题的解，这个也就需要返回值。
    并且分治过程中往往伴随着遍历，并不是说是分治就一定没有遍历。
    
    traverse的方法
    global variable: depth, 记录全局的最大深度

    divide-conquer： 最大区别是要返回一个value 
    """
    def maxDepth(self, root):
        if root is None:
            return 0
        # 求左子树的深度，右子树的深度，然后两者最大值 + 1 （1是根节点）
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1

    def maxDepth2(self, root):
        # write your code here
        self.depth = 0
        self.traverse(root, 1)
        return self.depth

    def traverse(self, root, cur_depth):
        if root is None:
            return
        # 走到一个实际的节点，可以把这个节点的深度和全局最优值去比较一下
        #  self.depth = max(self.depth, cur_depth)  放在这里或者放在最后一行，下面的中间都可以，前，后，中序遍历
        self.depth = max(self.depth, cur_depth)
        self.traverse(root.left, cur_depth + 1)
        self.traverse(root.right, cur_depth + 1)

