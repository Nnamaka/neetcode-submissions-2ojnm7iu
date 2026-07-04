# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def get_max_gain(node) -> int:
            if not node:
                return 0

            left_gain = max(get_max_gain(node.left), 0)
            right_gain = max(get_max_gain(node.right), 0)


            current_path_sum = node.val + left_gain + right_gain
            
            # Update our global maximum if the current path is better
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # For the parent call, return the maximum gain the node can extend.
            # It can only choose ONE branch (left or right) to continue the path.
            return node.val + max(left_gain, right_gain)
            
        get_max_gain(root)
        return self.max_sum