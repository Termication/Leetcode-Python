class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        # Step 1: Find the minimum element in each row
        min_in_rows = [(min(row), row.index(min(row))) for row in matrix]

        lucky_numbers = []
        # Step 2: Check if the minimum in the row is also the maximum in its column
        for min_val, col_index in min_in_rows:
            if all(min_val >= matrix[row][col_index] for row in range(len(matrix))):
                lucky_numbers.append(min_val)

        return lucky_numbers