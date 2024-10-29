class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
    
        # Memoization table initialized to None
        dp = [[None for _ in range(n)] for _ in range(m)]

        def dfs(row, col):
            # If already computed, return the stored result
            if dp[row][col] is not None:
                return dp[row][col]
            
            # Possible directions (row-1, col+1), (row, col+1), (row+1, col+1)
            directions = [(-1, 1), (0, 1), (1, 1)]
            max_moves = 0
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] > grid[row][col]:
                    max_moves = max(max_moves, 1 + dfs(new_row, new_col))
            
            # Memoize the result
            dp[row][col] = max_moves
            return dp[row][col]
        
        # Start DFS from each cell in the first column
        result = max(dfs(row, 0) for row in range(m))
        return result
        