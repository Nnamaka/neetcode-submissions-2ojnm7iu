class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = False


        # Step 1:  Use first row and column as flags
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    if r == 0:
                        first_row_has_zero = True
                    else:
                        matrix[r][0] = 0
                    matrix[0][c] = 0
        
        # Step 2: Zero out cells based on markers (skip first row/col for now)
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # step 3: zero out the first column if needed
        if matrix[0][0] == 0:
            for r in range(m):
                matrix[r][0] = 0

        # step 4: zero out the first row if needed
        if first_row_has_zero:
            for c in  range(n):
                matrix[0][c] = 0
        