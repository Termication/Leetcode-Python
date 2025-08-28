class Solution(object):
    def sortMatrix(self, grid):
        """
        Sorts the diagonals of a square matrix according to the specified rules.
        """
        n = len(grid)

        def process_diagonal(start_r, start_c):
            # Determine if the diagonal is in the bottom-left triangle (or main)
            # This is true if the starting row is greater than or equal to the starting column.
            is_bottom_left_triangle = (start_r >= start_c)
            
            diagonal_elements = []
            r, c = start_r, start_c
            
            # 1. Extract elements from the diagonal
            while r < n and c < n:
                diagonal_elements.append(grid[r][c])
                r += 1
                c += 1
                
            # 2. Sort the elements based on the rule
            if is_bottom_left_triangle:
                # Non-increasing order (descending)
                diagonal_elements.sort(reverse=True)
            else:
                # Non-decreasing order (ascending)
                diagonal_elements.sort()
                
            # 3. Place the sorted elements back into the grid
            r, c = start_r, start_c
            idx = 0
            while r < n and c < n:
                grid[r][c] = diagonal_elements[idx]
                r += 1
                c += 1
                idx += 1

        # Process all diagonals starting from the first column (bottom-left triangle)
        for i in range(n):
            process_diagonal(i, 0)
            
        # Process all diagonals starting from the first row, skipping the main diagonal
        # as it was already processed in the loop above.
        for j in range(1, n):
            process_diagonal(0, j)
            
        return grid
            