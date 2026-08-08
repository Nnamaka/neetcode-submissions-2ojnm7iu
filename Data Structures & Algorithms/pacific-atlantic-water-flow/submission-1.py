class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r: int, c: int, visited: set, prev_height: int):
            # Base case 1: out of bounds, already visited, or water can't flow uphill
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or heights[r][c] < prev_height):
                return

            visited.add((r, c))

            # Explore 4 neighboring directions (flowing uphill)
            for dr, dc in [(1,0), (-1,0), (0, 1), (0, -1)]:
                dfs(r + dr, c + dc, visited, heights[r][c])

        
        # step 1: Start DFS from pacific and atlantic borders
        # vertical borders: left (pacific), right( atalantic)
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])

        # Horizontal borders: Top (pacific), Bottom (atlantic)
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        # step 2: Find cells that are in both ocean sets
        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])
        
        return result