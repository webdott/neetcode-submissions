# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        first = kth = head

        for _ in range(1, k):
            if not kth:
                break
            
            kth = kth.next
        
        if not kth:
            return head

        prev, curr = self.reverseKGroup(kth.next, k), first

        for i in range(k):
            temp = curr.next
            
            curr.next = prev
            prev = curr
            
            curr = temp

        return prev

