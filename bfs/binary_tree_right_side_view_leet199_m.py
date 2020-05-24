class Solution:
    '''
    Time complexity: O(n)
    Space complexity: O(n)
    Because breadth-first search visits the tree layer-by-layer, the queue will be at its largest immediately before
    visiting the largest layer. The size of this layer is 0.5n =O(n) in the worst case (a complete binary tree).
    '''
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return root

        res = []
        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i == size - 1:
                    res.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

        return res