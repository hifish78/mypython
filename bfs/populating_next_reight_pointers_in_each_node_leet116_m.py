from collections import deque
class Node:
    def __init__(self, val=0, left=None, right=None, next=Noe):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root):
        if root is None:
            return None

        # Initialize a queue data structure which contains
        # just the root of the tree

        #queue = deque([root])  # NOT queue = deque(root) , need iterable object!!!

        queue = deque()
        queue.append(root) # NOT queue.append([root]),

        while queue:
            # Note the size of the queue, need to calculate each time since it is changeable
            size = len(queue)

            # Iterate over all the nodes on the current level
            for i in range(size):
                # Pop a node from the front of the queue
                node = queue.popleft()
                # if the node is not the last one in this level, then assign the first one of this queue to its' next pointer
                # if the node is the last one in this level, then assign None to its next pointer
                if i != size - 1:
                    node.next = queue[0]
                else:
                    node.next = None
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
