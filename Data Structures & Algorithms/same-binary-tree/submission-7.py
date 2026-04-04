# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# # my first try using iterative BFS 
# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
#         stack = [(p, q)]
#         while stack:
#             pp, qq = stack.pop()

#             if not pp and not qq:
#                 continue
            
#             if not pp or not qq or pp.val != qq.val:
#                 return False

#             stack.append((pp.right, qq.right))
#             stack.append((pp.left, qq.left))
                   
                
#         return True

# recursive DFS
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        # 1
        if not p or not q:
            return False
        # 2
        if p.val != q.val:
            return False

        #1 and 2 can be condensed as follows
        # if not p or not q or p.val != q.val:
        #     return False

        # the recursive step
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

            
