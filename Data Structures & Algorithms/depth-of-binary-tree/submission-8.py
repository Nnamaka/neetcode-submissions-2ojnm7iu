# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# my solution
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0

#         depth = max( self.depth(root.left, 2), self.depth(root.right, 2)) 

#         return max(1, depth) 
    
#     def depth(self, root, count) -> int:
#         if not root:
#             return 0

#         maxNode = max( self.depth(root.left, count + 1), self.depth(root.right, count + 1))
        
#         return count if maxNode == 0 else maxNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))





