class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        """
        Calculate the maximum number of rows with all values equal after some flips.
        
        Args:
        matrix: List[List[int]] - m x n binary matrix
        
        Returns:
        int - Maximum number of rows with all values equal
        """
        patterns = Counter()

        for row in matrix:
            # Generate the flip pattern
            base_pattern = tuple(row)
            flipped_pattern = tuple(1 - cell for cell in row)
            
            # Increment the count for both the row and its flipped version
            patterns[base_pattern] += 1
            patterns[flipped_pattern] += 1
        
        return max(patterns.values())
        