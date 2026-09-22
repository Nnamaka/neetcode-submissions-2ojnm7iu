# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Hash map for O(1) index lookup in inorder array
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0

        def helper(in_left: int, in_right: int) -> Optional[TreeNode]:
            nonlocal pre_idx
            
            # Base case: no elements to construct subtree
            if in_left > in_right:
                return None

            # Pick current root from preorder
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1

            # Get root position in inorder array
            root_idx = inorder_map[root_val]

            # Build left subtree first, then right subtree (matches preorder sequence)
            root.left = helper(in_left, root_idx - 1)
            root.right = helper(root_idx + 1, in_right)

            return root

        return helper(0, len(inorder) - 1)