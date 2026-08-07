"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# class Solution:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
#         if not node:
#             return None

#         # Maps original node -> cloned node
#         old_to_new = {}

#         def dfs(curr_node: 'Node') -> 'Node':
#             if curr_node in old_to_new:
#                 return old_to_new[curr_node]

#             # step 1: create a clone for the current node
#             copy = Node(curr_node.val)
#             old_to_new[curr_node] = copy

#             # step 2: Recursively clone and attach all neighbors
#             for neighbor in curr_node.neighbors:
#                 copy.neighbors.append(dfs(neighbor))

#             return copy

#         return dfs(node)

from collections import deque
from typing import Optional

# Breadth First Search method
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: 
            return None


        old_to_new = { node: Node(node.val)}
        queue = deque([node])

        while queue:
            curr = queue.popleft()

            for neighbor in curr.neighbors:
                # if neighbor hasn't cloned yet, create it and queue it
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                    # connect the cloned current node to the cloned neighbor
                old_to_new[curr].neighbors.append(old_to_new[neighbor])

        return old_to_new[node]