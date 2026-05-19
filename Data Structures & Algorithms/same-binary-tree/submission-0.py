# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            length_1 = len(q1)
            length_2 = len(q2)

            if length_1 != length_2:
                return False

            for _ in range(length_1):
                n1 = q1.popleft()
                n2 = q2.popleft()

                if (n1 and not n2) or (n2 and not n1) or (n1 and n2 and n1.val != n2.val):
                    return False

                if n1:
                    q1.append(n1.left)
                    q1.append(n1.right)

                if n2:
                    q2.append(n2.left)
                    q2.append(n2.right)

        return len(q1) == len(q2)
