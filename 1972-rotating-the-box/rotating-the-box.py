class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        """
        Rotate the box 90 degrees clockwise and apply gravity to stones.
        
        Args:
            box: List[List[str]] - m x n matrix representing the box
            
        Returns:
            List[List[str]] - Rotated matrix
        """
        m, n = len(box), len(box[0])

        # Step 1: Simulate gravity
        for row in box:
            empty_idx = n - 1  # Start from the rightmost column
            for col in range(n - 1, -1, -1):  # Traverse the row backward
                if row[col] == '*':  # Obstacle
                    empty_idx = col - 1  # Reset empty index to left of obstacle
                elif row[col] == '#':  # Stone
                    row[col], row[empty_idx] = row[empty_idx], row[col]  # Swap stone and empty
                    empty_idx -= 1  # Move empty index to the left

        # Step 2: Rotate the matrix 90 degrees clockwise
        rotated_box = [[box[row][col] for row in range(m - 1, -1, -1)] for col in range(n)]
        return rotated_box
        