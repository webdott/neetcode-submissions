# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]

        def dfs(root: Optional[TreeNode], greatest: int):
            if not root:
                return

            if root.val >= greatest:
                res[0] += 1

            dfs(root.left, max(greatest, root.val))
            dfs(root.right, max(greatest, root.val))

        dfs(root, -math.inf)

        return res[0]