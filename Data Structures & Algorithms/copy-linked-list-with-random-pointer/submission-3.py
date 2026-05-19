"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        p, c = dummy, head

        c_m, r_m = {}, defaultdict(list)

        while c:
            new_node = Node(c.val)
            p.next = new_node

            if c in r_m:
                for node in r_m[c]:
                    node.random = p.next
            
            c_m[c] = p.next

            if c.random in c_m:
                p.next.random = c_m[c.random]
            elif c.random:
                r_m[c.random].append(p.next)

            p = p.next
            c = c.next

        return dummy.next