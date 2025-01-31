class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        def dfs(r, c, color):
            if r < 0 or r >= n or c < 0 or c >= n or grid[r][c] != 1:
                return 0
            grid[r][c] = color
            return 1 + dfs(r + 1, c, color) + dfs(r - 1, c, color) + dfs(r, c + 1, color) + dfs(r, c - 1, color)

        color = 2  # Start coloring from 2 to avoid confusion with original 1s and 0s
        island_sizes = {0: 0, 1:0} # size of 0 should also be tracked.
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    size = dfs(r, c, color)
                    island_sizes[color] = size
                    color += 1

        max_island = 0
        for size in island_sizes.values():
            max_island = max(max_island, size)


        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    adjacent_islands = set()
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            adjacent_islands.add(grid[nr][nc])

                    current_island_size = 1  # Start with the current cell as 1
                    for island_color in adjacent_islands:
                        current_island_size += island_sizes[island_color]
                    max_island = max(max_island, current_island_size)

        return max_island
        