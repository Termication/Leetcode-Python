class Solution(object):
    def lenOfVDiagonal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        n = len(grid)
        m = len(grid[0])
        directions = [(1,1), (1,-1), (-1,1), (-1,-1)]
        # Precompute f2_arr and f0_arr for each direction
        num_dirs = len(directions)
        f2_arr = [[[0] * m for _ in range(n)] for _ in range(num_dirs)]
        f0_arr = [[[0] * m for _ in range(n)] for _ in range(num_dirs)]
        
        for idx, d in enumerate(directions):
            dx, dy = d
            if dx == 1 and dy == 1:
                i_range = range(n-1, -1, -1)
                j_range = range(m-1, -1, -1)
            elif dx == 1 and dy == -1:
                i_range = range(n-1, -1, -1)
                j_range = range(0, m)
            elif dx == -1 and dy == 1:
                i_range = range(0, n)
                j_range = range(m-1, -1, -1)
            else:
                i_range = range(0, n)
                j_range = range(0, m)
            
            for i in i_range:
                for j in j_range:
                    ni = i + dx
                    nj = j + dy
                    if ni < 0 or ni >= n or nj < 0 or nj >= m:
                        if grid[i][j] == 2:
                            f2_arr[idx][i][j] = 1
                        else:
                            f2_arr[idx][i][j] = 0
                        if grid[i][j] == 0:
                            f0_arr[idx][i][j] = 1
                        else:
                            f0_arr[idx][i][j] = 0
                    else:
                        if grid[i][j] == 2:
                            f2_arr[idx][i][j] = 1 + f0_arr[idx][ni][nj]
                        else:
                            f2_arr[idx][i][j] = 0
                        if grid[i][j] == 0:
                            f0_arr[idx][i][j] = 1 + f2_arr[idx][ni][nj]
                        else:
                            f0_arr[idx][i][j] = 0
                            
        best = 0
        new_idx_map = [1, 3, 0, 2]  # mapping from original direction index to new direction index for clockwise 90 turn
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    for idx, d in enumerate(directions):
                        dx, dy = d
                        ni = i + dx
                        nj = j + dy
                        if ni >= 0 and ni < n and nj >= 0 and nj < m:
                            straight = 1 + f2_arr[idx][ni][nj]
                        else:
                            straight = 1
                        if straight > best:
                            best = straight
                        for t in range(1, straight):
                            x = i + t * dx
                            y = j + t * dy
                            new_d = (dy, -dx)
                            new_idx = new_idx_map[idx]
                            nx = x + new_d[0]
                            ny = y + new_d[1]
                            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                                add = 0
                            else:
                                if (t+1) % 2 == 1:
                                    add = f2_arr[new_idx][nx][ny]
                                else:
                                    add = f0_arr[new_idx][nx][ny]
                            total = t + 1 + add
                            if total > best:
                                best = total
        return best
        