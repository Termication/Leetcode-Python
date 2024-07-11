class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create a list to hold each row's string
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        # Iterate through each character in the string
        for char in s:
            rows[current_row] += char
            # If we are in the first or last row, we should change direction
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            # Move to the next row
            current_row += 1 if going_down else -1
        
        # Combine all rows to form the final string
        return ''.join(rows)