# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid:
#             return 0

#         ROWS, COLS = len(grid), len(grid[0])
#         island_count = 0

#         def dfs(r: int, c: int):
#             # Base Case: Out of bounds or hit a water cell ('0')
#             if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == '0':
#                 return

#             # sink the land: Mark as visited by turning it into water
#             grid[r][c] = '0'

#             # Explore all 4 adjacent directions
#             dfs(r + 1, c) # Down
#             dfs(r - 1, c) # Up
#             dfs(r, c + 1) # Right
#             dfs(r, c - 1) # left

#         # iterate through every cell in the matrix
#         for r in range(ROWS):
#             for c in range(COLS):
#                 if grid[r][c] == '1':

#                     # found a brand new island
#                     island_count += 1
#                     dfs(r, c)
#         return island_count


from collections import deque

class Solution:
    def numIslands(self, grid: List[list[str]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        island_count = 0


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    island_count += 1

                    # start BFS
                    queue = deque([(r,c)])
                    grid[r][c] = '0'

                    while queue:
                        row, col = queue.popleft()

                        # check neighbors
                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nr, nc = row + dr, col + dc
                            if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == '1':
                                queue.append((nr, nc))
                                grid[nr][nc] = '0' #sink it right away
        return island_count