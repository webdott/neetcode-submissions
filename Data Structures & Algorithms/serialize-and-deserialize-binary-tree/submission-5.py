# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "-"

        res = [str(root.val)]
        q = deque([root])
        m = {root.val: 0}

        while q:
            l = len(q)

            for _ in range(l):
                node = q.popleft()
                curr_idx = len(res) - 1
                left_idx = curr_idx + 1
                right_idx = curr_idx + 2

                res[m[node.val]] += ("^" + str(left_idx) + "^" + str(right_idx))
                res.append(str(node.left.val) if node.left else "-")
                res.append(str(node.right.val) if node.right else "-")

                if node.left:
                    m[node.left.val] = left_idx
                    q.append(node.left)
                if node.right:
                    m[node.right.val] = right_idx
                    q.append(node.right)

        return "$".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tree = data.split("$")

        def dfs(idx: int) -> Optional[TreeNode]:
            if idx >= len(tree) or tree[idx] == "-":
                return None

            node_val, left_idx, right_idx = tree[idx].split("^")

            root_val = int(node_val)
            root = TreeNode(root_val)

            root.left = dfs(int(left_idx))
            root.right = dfs(int(right_idx))

            return root

        return dfs(0)

        return None

