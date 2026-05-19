# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        res = []
        q = deque([root])

        while q:
            l = len(q)
            inner = []

            for i in range(l):
                v = q.popleft()
                inner.append(v.val)

                if v.left:
                    q.append(v.left)

                if v.right:
                    q.append(v.right)

            res.append(inner)

        return res

