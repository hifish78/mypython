# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # edge case
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        mid = self.findMid(head)
        node = TreeNode(mid.val)
        # from head to mid -1
        node.left = self.sortedListToBST(head)
        # from mid+1 to tail
        node.right = self.sortedListToBST(mid.next)

        return node

    def findMid(self, head):
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        return slow


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

sol = Solution()
res = sol.findMid(head)
sol.sortedListToBST(head)