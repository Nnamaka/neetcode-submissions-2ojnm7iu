# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        q = collections.deque()
        q.append((root, float('-inf'), float('inf')))

        while q:
            qlen = len(q)

            for i in range(qlen):
                node, low, high = q.popleft()

                # 1. Validate the current node against its inherited strict boundaries
                if not (low < node.val < high):
                    return False

                # 2. When appending the left child, update the upper bound to node.val
                if node.left:
                    q.append((node.left, low, node.val))
                    
                # 3. When appending the right child, update the lower bound to node.val
                if node.right:
                    q.append((node.right, node.val, high))

        return True






