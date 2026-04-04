# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        

        stack = [(p, q)]
        while stack:
            pp, qq = stack.pop()

            if not pp and not qq:
                continue
            
            if not pp or not qq or pp.val != qq.val:
                return False

            stack.append((pp.right, qq.right))
            stack.append((pp.left, qq.left))
                   
                
        return True

            

               

            
