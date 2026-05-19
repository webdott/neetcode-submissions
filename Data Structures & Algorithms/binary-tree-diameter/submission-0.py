# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_ = 0

    def recur(self, root: Optional[TreeNode]):
        if not root:
            return 0

        left = self.recur(root.left)
        right = self.recur(root.right)

        self.max_ = max(self.max_, left + right)

        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.recur(root)

        return self.max_