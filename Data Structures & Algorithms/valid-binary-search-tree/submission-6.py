# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def bfs(root: Optional[TreeNode]) -> (bool, Optional[int], Optional[int]):
            if not root:
                return (True, None, None)

            l, i, j = bfs(root.left)
            r, k, m = bfs(root.right)

            a, b = root.val, root.val
            
            if i and j:
                a, b = min(a, i, j), max(b, i, j)
            else:
                i, j = float('-inf'), float('-inf')

            if k and m:
                a, b = min(a, k, m), max(b, k, m)
            else:
                k, m = float('inf'), float('inf')

            if l and r:
                if root.val <= i or root.val <= j:
                    return (False, a, b)

                if root.val >= k or root.val >= m:
                    return (False, a, b)

                return (True, a, b)

            return (False, a, b)

        res, a, b = bfs(root)

        return res