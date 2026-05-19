# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findIdxOfRoot(self, i: int, inorder: List[int]) -> int:
        for (idx, num) in enumerate(inorder):
            if num == i:
                return idx

        return -1

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        if len(preorder) == 1:
            return root

        n, m = len(inorder), len(preorder)
        inorder_set = {}

        for i in range(n):
            num = inorder[i]
            inorder_set[num] = i

        idx_of_root = inorder_set[root_val]

        left_list = inorder[0:idx_of_root]
        right_list = inorder[idx_of_root+1:]
        left_set = set(left_list)
        right_set = set(right_list)

        p_idx = 1

        while p_idx < m and preorder[p_idx] in left_set:
            p_idx += 1

        root.left = self.buildTree(preorder[1:p_idx], left_list)
        root.right = self.buildTree(preorder[p_idx:], right_list)

        return root


        