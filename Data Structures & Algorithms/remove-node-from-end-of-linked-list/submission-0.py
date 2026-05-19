# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0

        curr = head

        while curr:
            l += 1
            curr = curr.next

        i = 0
        prev, curr = None, head

        while i < l - n:
            i += 1
            prev = curr
            curr = curr.next

        if not prev:
            return curr.next
        
        prev.next = curr.next
        curr = None

        return head