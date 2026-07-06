class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def backtrack(r: int, c: int, index: int) -> bool:
            if index == len(word):
                return True

            if ( r < 0 or c < 0 or r >= ROWS or c >= COLS or
                board[r][c] != word[index]):
                return False

            temp = board[r][c]
            board[r][c] = '#'

            # step 2: Explore all 4 adjacent directions
            found = (backtrack(r + 1, c, index + 1) or
                    backtrack(r - 1, c, index + 1) or
                    backtrack(r, c + 1, index + 1) or
                    backtrack(r, c - 1, index + 1))

            board[r][c] = temp

            return found
        
        # scan the entire grid to find a starting point matching the first
        # letter

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if backtrack(r, c, 0):
                        return True
        
        return False