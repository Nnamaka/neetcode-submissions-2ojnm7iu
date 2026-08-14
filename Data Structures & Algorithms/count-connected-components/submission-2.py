from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # step 1: Build the adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(node: int):
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        components = 0

        # step 2: Iterate through all notes
        for i in range(n):
            if i not in visited:
                components += 1
                visited.add(i)
                dfs(i) # Traverses and marks the Entire connected component
        return components

        
