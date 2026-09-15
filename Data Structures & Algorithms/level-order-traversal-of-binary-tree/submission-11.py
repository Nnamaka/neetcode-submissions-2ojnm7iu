# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         result = []

#         # use python deque datastructure
#         q = collections.deque()
#         q.append(root)

#         while q:
#             qlen = len(q)
#             level = []

#             for i in range(qlen):
#                 node = q.popleft()
#                 if node:
#                     level.append(node.val)
#                     if node.left:
#                         q.append(node.left)
#                     if node.right:
#                         q.append(node.right)
#             if level:
#                 result.append(level)
#         return result


from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        # first-in-first-out (FIFO)
        queue = []
        queue.append(root)

        while queue:
            lenq = len(queue)
            level = []

            for i in range(lenq):
                node = queue.pop(0)
                
                if node:
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            if level:
                result.append(level)

        return result