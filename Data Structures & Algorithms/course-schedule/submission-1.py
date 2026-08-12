from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # not, this creates a dictionary of a list as the key, and an int as the value
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[pre].append(crs)

        # 0 = Unvisited, 1 = Visiting, 2 = Visited
        state = [0] * numCourses

        def dfs(crs: int) -> bool:
            if state[crs] == 1:
                return False
            if state[crs] == 2:
                return True

            state[crs] = 1

            for neighbor in adj[crs]:
                if not dfs(neighbor):
                    return False

            state[crs] = 2 # mark as fully processed
            return True

        for i in range(numCourses):
            if state[i] == 0:
                if not dfs(i):
                    return False
        return True
        