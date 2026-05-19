# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        c1, c2, p, carry = l1, l2, dummy, 0

        while c1 and c2:
            s = c1.val + c2.val + carry
            carry = s // 10
            p.next = ListNode(s % 10)
            c1 = c1.next
            c2 = c2.next
            p = p.next

        while c1:
            s = c1.val + carry
            carry = s // 10
            p.next = ListNode(s % 10)
            p = p.next
            c1 = c1.next

        while c2:
            s = c2.val + carry
            carry = s // 10
            p.next = ListNode(s % 10)
            p = p.next
            c2 = c2.next

        if carry > 0:
            p.next = ListNode(carry)

        return dummy.next