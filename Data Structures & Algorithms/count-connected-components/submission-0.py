class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n
        components = n

        def find(node: int) -> int:
            if parent[node] != node:
                parent[node] = find(parent[node]) # path compression
            return parent[node]

        def union(n1: int, n2: int) -> int:
            root1, root2 = find(n1), find(n2)

            # if they already belong to the same component, no reduction
            if root1 == root2:
                return 0

            # union by rank optimization
            if rank[root1] > rank[root2]:
                parent[root2] = root1
                rank[root1] += rank[root2]
            else:
                parent[root1] = root2
                rank[root2] += rank[root1]

            return 1

        for u, v in edges: 
            components -= union(u, v)
        
        return components
        