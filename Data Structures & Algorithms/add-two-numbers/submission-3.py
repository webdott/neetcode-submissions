# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def recur(l1: Optional[ListNode], l2: Optional[ListNode], carry: int) -> Optional[ListNode]:
            if not l1 and not l2 and not carry:
                return None

            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            s = l1_val + l2_val + carry
            carry = s // 10
            curr = ListNode(s % 10)
            curr.next = recur(l1.next if l1 else None, l2.next if l2 else None, carry)

            return curr

        return recur(l1, l2, 0)

    def addTwoNumbersIter(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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