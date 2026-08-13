from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # condition 1: A tree with 'n' nodes must have 'n-1' edges
        if len(edges) != n - 1:
            return False
        
        # Build adjacency list
        adj = defaultdict(list)
        for u, v in edges: 
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(node: int, parent: int) -> bool:
            if node in visited:
                return False # cycle detected!

            visited.add(node)

            for neighbor in adj[node]:
                # skip the node we immediately came from
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False

            return True

        # check for cycles starting from node 0
        if not dfs(0, -1):
            return False

        # condition 2: Graph must be fully connectd
        return len(visited) == n








