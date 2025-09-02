class Solution(object):
    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        if n == 0:
            return 0
        
        xs = sorted(set(x for x, y in points))
        ys = sorted(set(y for x, y in points))
        x_map = {x: i for i, x in enumerate(xs)}
        y_map = {y: i for i, y in enumerate(ys)}
        
        n_x = len(xs)
        n_y = len(ys)
        
        grid = [[0] * n_y for _ in range(n_x)]
        for x, y in points:
            i = x_map[x]
            j = y_map[y]
            grid[i][j] = 1
            
        P = [[0] * (n_y + 1) for _ in range(n_x + 1)]
        for i in range(n_x):
            for j in range(n_y):
                P[i+1][j+1] = grid[i][j] + P[i][j+1] + P[i+1][j] - P[i][j]
                
        points_indices = []
        for x, y in points:
            ix = x_map[x]
            iy = y_map[y]
            points_indices.append((ix, iy))
            
        count = 0
        for i in range(n):
            A = points[i]
            ix1, iy2 = points_indices[i]
            for j in range(n):
                if i == j:
                    continue
                B = points[j]
                if A[0] <= B[0] and A[1] >= B[1]:
                    ix2, iy1 = points_indices[j]
                    total = P[ix2+1][iy2+1] - P[ix1][iy2+1] - P[ix2+1][iy1] + P[ix1][iy1]
                    if total == 2:
                        count += 1
        return count