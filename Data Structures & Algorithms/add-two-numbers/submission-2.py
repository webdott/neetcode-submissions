# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        c1, c2, p, carry = l1, l2, dummy, 0

        while c1 or c2 or carry:
            c1_val = c1.val if c1 else 0
            c2_val = c2.val if c2 else 0
            s = c1_val + c2_val + carry
            carry = s // 10
            p.next = ListNode(s % 10)

            if c1:
                c1 = c1.next
            if c2:
                c2 = c2.next

            p = p.next

        return dummy.next