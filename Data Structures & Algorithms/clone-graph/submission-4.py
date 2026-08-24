"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        h1, h2 = node, Node(node.val)
        q1, q2 = deque([h1]), deque([h2])
        s1, s2 = set([h1]), {h2.val: h2}

        while q1:
            c1, c2 = q1.popleft(), q2.popleft()

            for n1 in c1.neighbors:
                if n1 not in s1:
                    q1.append(n1)
                    n2 = Node(n1.val)
                    q2.append(n2)
                    s1.add(n1)
                    s2[n2.val] = n2
                else:
                    n2 = s2[n1.val]

                c2.neighbors.append(n2)

        return h2