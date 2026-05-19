# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        n, m = len(inorder), len(preorder)
        inorder_set = {}

        for i in range(n):
            num = inorder[i]
            inorder_set[num] = i

        idx_of_root = inorder_set[root_val]

        root.left = self.buildTree(preorder[1:idx_of_root + 1], inorder[0:idx_of_root])
        root.right = self.buildTree(preorder[idx_of_root + 1:], inorder[idx_of_root+1:])

        return root


        