# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root

        while cur or stack:

            # move to the deepest left-most part of the tree
            while cur:
                stack.append(cur)
                cur = cur.left

            # process the current node
            cur = stack.pop()

            # decrement k to mark our position
            k -= 1

            # check if we have our kth value
            if k == 0 :
                return cur.val
            
            cur = cur.right



