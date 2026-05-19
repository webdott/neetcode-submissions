# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        res_dict = {}

        for ls in lists:
            curr = ls

            while curr:
                key = curr.val
                if key not in res_dict:
                    n = ListNode(0)
                    res_dict[key] = [n, n]

                e_ls, tail = res_dict[key]
                tail.next = curr

                res_dict[key] = [e_ls, tail.next]

                curr = curr.next

        res_dict = dict(sorted(res_dict.items()))

        res = ListNode(0)
        curr = res

        for key in res_dict:
            curr.next = res_dict[key][0].next
            curr = res_dict[key][1]

        return res.next
                


