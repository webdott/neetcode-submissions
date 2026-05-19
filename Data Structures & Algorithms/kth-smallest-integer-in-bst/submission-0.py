# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root:Optional[TreeNode], k:int, li:[int]) -> int:
            if not root:
                return -1

            dfs(root.left, k, li)

            li.append(root.val)

            if len(li) >= k:
                return li[k - 1]

            dfs(root.right, k, li)

            if len(li) >= k:
                return li[k - 1]
            else:
                return -1


        return dfs(root, k, [])