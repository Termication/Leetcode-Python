class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        # Directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = []
        steps = 1  # initial steps to take in one direction
        x, y = rStart, cStart
        result.append([x, y])
        
        if rows * cols == 1:
            return result
        
        while len(result) < rows * cols:
            for i in range(4):
                dx, dy = directions[i]
                for _ in range(steps):
                    x += dx
                    y += dy
                    if 0 <= x < rows and 0 <= y < cols:
                        result.append([x, y])
                # After two directions (right & down, or left & up), increment step size
                if i % 2 == 1:
                    steps += 1
        
        return result