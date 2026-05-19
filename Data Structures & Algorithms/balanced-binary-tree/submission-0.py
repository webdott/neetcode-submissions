# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True

        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal res

            if not res:
                return 0

            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            res = res and abs(left - right) <= 1

            return 1 + max(left, right)

        dfs(root)

        return res