class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
要点： 
1）dummy head to simplify the code. without dummy head, you would have to write extra conditional statements to 
initialize the head's value
2) x = l1.val if l1 is not None else 0 , by doing that, no need to check whih linklist is longer
3) considering carry 
4) cur = cur.next should be put before checking "carry != 0"
"""
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        type: l1 ListNode
        type: l2 ListNode
        rtype: ListNode
        """
        dummyHead = ListNode()
        cur = dummyHead
        carry = 0
        while l1 or l2:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            total = x + y + carry
            carry = total // 10
            value = total % 10
            cur.next = ListNode(value)
            cur = cur.next  # cur = cur.next should be put before "if carry != 0" !!!
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if carry != 0:
                cur.next = ListNode(carry)
        return dummyHead.next
