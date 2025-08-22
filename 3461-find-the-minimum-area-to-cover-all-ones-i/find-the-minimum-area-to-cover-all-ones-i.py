import math

class Solution(object):
    def minimumArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        
        # Use float('inf') for compatibility with older Python versions
        min_row = float('inf')
        max_row = float('-inf')
        min_col = float('inf')
        max_col = float('-inf')
        
        found_one = False
        
        # Iterate through the grid to find the boundaries of the 1s
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    found_one = True
                    min_row = min(min_row, r)
                    max_row = max(max_row, r)
                    min_col = min(min_col, c)
                    max_col = max(max_col, c)
                    
        # If no 1s were found, the area is 0
        if not found_one:
            return 0
            
        # Calculate height and width of the bounding box
        # The boundaries will be floats after min/max with float('inf')
        # so we cast them back to integers.
        height = int(max_row - min_row + 1)
        width = int(max_col - min_col + 1)
        
        return height * width