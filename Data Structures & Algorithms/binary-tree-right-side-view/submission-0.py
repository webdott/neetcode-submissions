# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode], ) -> List[int]:
        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            l = len(q)
            added = False
            
            for i in range(l):
                v = q.popleft()

                if not added:
                    res.append(v.val)
                    added = True

                if v.right:
                    q.append(v.right)

                if v.left:
                    q.append(v.left)

        return res
